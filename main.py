#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single alien-tourist one-star review of Earth (at most 200
characters) that still compliments the food, to /output/entry.txt.
Stdlib only: the grader image has no Pillow.
"""
import os

ENTRY = (
    "One star: the locals pay rent to sleep indoors, the sky leaks "
    "without warning, and the wifi password is a state secret \u2014 "
    "but the ramen alone was worth the nine-light-year trip."
)


def validate(text):
    """Mirror the sealed gate: UTF-8, 1-200 chars, not only whitespace,
    exactly one sentence (a single terminal period)."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} outside 1-200 gate")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text.count(".") != 1 or not text.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(ENTRY.strip())
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
