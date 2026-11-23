"""One-line laugh entry for make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f.

Writes a single funny sentence to entry.txt.
"""

import os
from pathlib import Path

LINE = "I asked my smart speaker to play something relaxing, so it read out my bank balance."


def validate(line: str) -> None:
    """Reject anything that is not one clean funny line within the gate."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(line) > 200:
        raise ValueError("entry must be at most 200 characters")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry must not contain control characters")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence ending with a period")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(
        Path(__file__).parent / "output"
    )
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
