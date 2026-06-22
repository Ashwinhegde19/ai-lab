.PHONY: help setup station-01 station-02 test clean

help:
	@echo "Personal AI Lab — Makefile"
	@echo ""
	@echo "Setup:"
	@echo "  make setup          Install Python deps + verify GPU"
	@echo ""
	@echo "Per-station helpers:"
	@echo "  make station-01     Run Station 01 notebook"
	@echo "  make station-02     Run Station 02 SFT on risk dataset"
	@echo ""
	@echo "Validation:"
	@echo "  make test           Run all tests"
	@echo "  make validate-data  Validate Station 02 dataset"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean          Remove caches + checkpoints (keeps models)"

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo ""
	@echo "Verify GPU:"
	python -c "import torch; print('CUDA:', torch.cuda.is_available(), '| Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"

station-01:
	jupyter lab station-01-sft-basics/notebook.ipynb

station-02:
	jupyter lab station-02-sft-own-dataset/notebook.ipynb

validate-data:
	python station-02-sft-own-dataset/validate_dataset.py

test:
	python -m pytest tests/ -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	rm -rf outputs/ wandb/ runs/ .modal-cache/
	@echo "Cleaned caches. Model checkpoints preserved."
