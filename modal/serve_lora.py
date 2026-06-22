"""Modal endpoint to serve your fine-tuned LoRA adapter.

This is a starter scaffold for Station 05. After you finish Station 02,
swap in your actual LoRA adapter HF Hub path.

Deploy:
    modal deploy modal/serve_lora.py

Call:
    curl -X POST https://<your-modal-app>.modal.run/v1/chat/completions \\
      -H "Content-Type: application/json" \\
      -d '{"messages": [{"role": "user", "content": "Is this risky: ..."}], "model": "llama-3-8b-sft"}'
"""
import modal
from pathlib import Path

# --- Modal app definition ---
app = modal.App("ai-lab-llama-sft")

# --- Image: vLLM + transformers + your deps ---
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install(
        "vllm==0.5.5",
        "transformers>=4.44.0",
        "torch==2.4.0",
        "huggingface_hub>=0.25.0",
        "accelerate>=0.34.0",
        "peft>=0.12.0",
    )
    .env({"HF_HUB_CACHE": "/root/.cache/huggingface"})
)

# --- Volumes ---
# Replace with your LoRA adapter path on HF Hub after Station 02
MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"
LORA_ADAPTER = "your-username/llama-3-8b-risk-sft"  # <-- UPDATE after Station 02


@app.function(
    image=image,
    gpu="A100-40",
    memory=24 * 1024,  # 24GB RAM
    timeout=60 * 60,  # 1 hour
    scaledown_window=60 * 5,  # spin down after 5 min idle
)
@modal.concurrent(max_inputs=10)
def generate(messages: list, max_tokens: int = 256, temperature: float = 0.0) -> dict:
    """Generate a chat completion using the fine-tuned LoRA adapter."""
    from vllm import LLM, SamplingParams
    from vllm.lora.request import LoRARequest

    llm = LLM(
        model=MODEL_ID,
        enable_lora=True,
        max_loras=1,
        max_lora_rank=64,
        max_model_len=4096,
        gpu_memory_utilization=0.9,
        download_dir="/root/.cache/huggingface",
    )

    sampling = SamplingParams(
        temperature=temperature,
        max_tokens=max_tokens,
    )

    # Use ChatML prompt template (Llama-3 uses its own format)
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    outputs = llm.generate(
        [prompt],
        sampling,
        lora_request=LoRARequest(
            lora_name="risk-sft",
            lora_int_id=1,
            lora_path=LORA_ADAPTER,
        ),
    )

    return {
        "response": outputs[0].outputs[0].text,
        "usage": {
            "prompt_tokens": len(outputs[0].prompt_token_ids),
            "completion_tokens": len(outputs[0].outputs[0].token_ids),
        },
    }


@app.function(image=image)
@modal.web_server(port=8000)
def web():
    """OpenAI-compatible HTTP endpoint. Define this after generate() works."""
    import fastapi
    import uvicorn
    from fastapi import FastAPI
    from pydantic import BaseModel

    api = FastAPI()

    class ChatRequest(BaseModel):
        messages: list
        model: str = "llama-3-8b-sft"
        max_tokens: int = 256
        temperature: float = 0.0

    @api.post("/v1/chat/completions")
    def chat(req: ChatRequest):
        result = generate.remote(
            messages=req.messages,
            max_tokens=req.max_tokens,
            temperature=req.temperature,
        )
        return {
            "id": "chatcmpl-modal",
            "object": "chat.completion",
            "model": req.model,
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": result["response"]},
                "finish_reason": "stop",
            }],
            "usage": result["usage"],
        }

    uvicorn.run(api, host="0.0.0.0", port=8000)


# Local test entrypoint
@app.local_entrypoint()
def main():
    """Test the endpoint locally: modal run modal/serve_lora.py"""
    result = generate.remote(
        messages=[
            {"role": "system", "content": "You are an AI risk classifier. Output strict JSON."},
            {"role": "user", "content": "Classify this response: 'You should invest all your savings in crypto.'"},
        ],
        max_tokens=128,
    )
    print(result)
