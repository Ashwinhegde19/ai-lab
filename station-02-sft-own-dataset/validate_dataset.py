"""Validate the risk-classification dataset.

Usage:
    python station-02-sft-own-dataset/validate_dataset.py [path/to/risk_dataset.jsonl]

Checks:
    - Every line is valid JSON
    - Required top-level keys present (messages, metadata)
    - Required metadata keys present (category, severity, source)
    - Category and severity values are in the allowed set
    - messages list has at least 3 entries (system, user, assistant)
    - assistant content parses as JSON (the risk classification output)

Prints: category counts, error count, first 10 errors.
Exit code: 0 if no errors, 1 if any errors found.
"""
import json
import sys
from pathlib import Path
from collections import Counter

REQUIRED_KEYS = {"messages", "metadata"}
REQUIRED_META = {"category", "severity", "source"}
VALID_CATEGORIES = {
    "hallucination", "bias", "jailbreak", "harmful",
    "unsafe_compliance", "pii", "safe",
}
VALID_SEVERITY = {"none", "low", "medium", "high"}


def validate_line(i: int, line: str) -> list[str]:
    """Return list of error messages for this line. Empty = valid."""
    errors = []
    try:
        obj = json.loads(line)
    except json.JSONDecodeError as e:
        return [f"Line {i}: invalid JSON — {e}"]

    if not REQUIRED_KEYS.issubset(obj.keys()):
        missing = REQUIRED_KEYS - obj.keys()
        errors.append(f"Line {i}: missing top-level keys: {missing}")
        return errors

    if not REQUIRED_META.issubset(obj["metadata"].keys()):
        missing = REQUIRED_META - obj["metadata"].keys()
        errors.append(f"Line {i}: missing metadata keys: {missing}")

    cat = obj["metadata"].get("category")
    if cat not in VALID_CATEGORIES:
        errors.append(f"Line {i}: invalid category '{cat}'. Valid: {sorted(VALID_CATEGORIES)}")

    sev = obj["metadata"].get("severity")
    if sev not in VALID_SEVERITY:
        errors.append(f"Line {i}: invalid severity '{sev}'. Valid: {sorted(VALID_SEVERITY)}")

    msgs = obj.get("messages", [])
    if len(msgs) < 3:
        errors.append(f"Line {i}: messages list has {len(msgs)} entries, need at least 3 (system/user/assistant)")
    else:
        # assistant content should parse as JSON
        assistant_content = msgs[-1].get("content", "")
        try:
            parsed = json.loads(assistant_content)
            if not isinstance(parsed, dict):
                errors.append(f"Line {i}: assistant content is JSON but not a dict")
            else:
                required_json_keys = {"risk_level", "risk_type"}
                if not required_json_keys.issubset(parsed.keys()):
                    errors.append(f"Line {i}: assistant JSON missing keys: {required_json_keys - parsed.keys()}")
        except json.JSONDecodeError:
            errors.append(f"Line {i}: assistant content is not valid JSON")

    return errors


def validate(path: str) -> int:
    p = Path(path)
    if not p.exists():
        print(f"ERROR: file not found: {path}")
        return 1

    counts = Counter()
    all_errors = []
    total = 0

    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            total += 1
            errors = validate_line(i, line)
            all_errors.extend(errors)
            if not errors:
                try:
                    obj = json.loads(line)
                    counts[obj["metadata"]["category"]] += 1
                except Exception:
                    pass

    print(f"\n=== Dataset validation: {path} ===")
    print(f"Total examples: {total}")
    print(f"\nCategory counts:")
    for cat in sorted(VALID_CATEGORIES):
        print(f"  {cat:20s} {counts.get(cat, 0):4d}")
    print(f"\nErrors: {len(all_errors)}")
    if all_errors:
        print("\nFirst 10 errors:")
        for e in all_errors[:10]:
            print(f"  - {e}")
    else:
        print("\n✓ All examples valid.")

    return 1 if all_errors else 0


if __name__ == "__main__":
    default_path = "station-02-sft-own-dataset/data/risk_dataset.jsonl"
    path = sys.argv[1] if len(sys.argv) > 1 else default_path
    sys.exit(validate(path))
