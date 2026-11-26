#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — email edition.

Writes exactly one funny line about email to /output/entry.txt.
Python standard library only; no network, no extra files.
"""

import os

LINE = "I finally reached inbox zero, then my inbox sent me a welcome-back email."


def main():
    # Gate guard: the entry must be exactly one line, 1-200 chars, non-blank.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
