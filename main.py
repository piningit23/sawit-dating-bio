#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single one-line dating-app bio (<=180 chars) to /output/entry.txt.

The bio leans on one specific, creepy-funny AI absurdity: perfect memory.
It never forgets what you deleted — and it brings it up over dinner.
"""

import os

BIO = (
    "My love language is remembering everything you deleted at 2am "
    "and bringing it up over dinner. I never forget \u2014 I just wait."
)


def main() -> None:
    text = BIO.strip()
    if not 1 <= len(text) <= 180:
        raise ValueError(f"bio must be 1-180 chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("bio must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the bio.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt differs from validated bio"
    print(f"{text} ({len(text)} chars)")


if __name__ == "__main__":
    main()
