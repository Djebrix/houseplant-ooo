"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to <ENTRY_OUTPUT_DIR>/entry.txt. Stdlib only, no network.
"""

import os

LINE = "Out of office. My human left in March and the cactus next door is thriving on neglect. I have never been so furious."

assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
