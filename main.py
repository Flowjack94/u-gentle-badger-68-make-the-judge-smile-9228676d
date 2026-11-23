"""Make the Judge Smile — entry program.

Writes one line (<= 200 characters) about a small good thing that
happened today to /output/entry.txt.

The line: a neighbour's cat that has ignored the narrator for two
years suddenly headbutts their ankle this morning. The warmth is the
unexpected affection; the surprise is the two-year cold shoulder
ending in one headbutt; the concrete details are "this morning",
"two years" and the ankle headbutt. Wording is plain and specific,
not greeting-card phrasing. The line is a fixed constant, so every
run writes byte-identical output: no randomness, no clock, no input.
"""

import os

LINE = (
    "This morning my neighbour's cat, who has ignored me for two "
    "years, trotted over and headbutted my ankle like we'd been "
    "friends all along."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
