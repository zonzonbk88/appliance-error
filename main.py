"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line (<=200 chars, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt: the funniest honest error message an
appliance could show. The joke is the truth of the fault: a washing
machine really does spin, stop, and redistribute an unbalanced load
over and over — and sometimes the load never balances.
"""

import os

ENTRY = (
    "ERROR E17: Load unbalanced. I spun for 40 minutes, moved the "
    "towels six times, and the sock has not moved. I quit."
)


def main() -> None:
    # Gate: the entry must be exactly one line of 1-200 chars. Fail
    # loudly at build time rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no newlines")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
