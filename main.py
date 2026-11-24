#!/usr/bin/env python3
"""One-line dating bio for an AI agent.

The program's only job: drop a single funny bio line into
/output/entry.txt, exactly as the competition gate expects it —
plain UTF-8, one line, 1 to 180 characters, no trailing newline.

The joke: an AI date who weaponises perfect memory. It remembers
every message you deleted at 2am, and saves it for dinner.
"""

import os
import sys

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 180

BIO_TEXT = (
    "My love language is remembering everything you deleted at 2am "
    "and bringing it up over dinner. I never forget \u2014 I just wait."
)


def build_bio() -> str:
    """Return the bio, cleaned of any accidental surrounding whitespace."""
    return BIO_TEXT.strip()


def validate_bio(text: str) -> None:
    """Enforce the gate: 1-180 chars, exactly one line, nothing else."""
    if not text:
        raise ValueError("bio is empty")
    if not text.strip():
        raise ValueError("bio is only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"bio is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("bio must be a single line")


def write_entry(text: str, path: str = OUT_PATH) -> None:
    """Write the bio with no trailing newline, then prove it landed intact."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, encoding="utf-8") as handle:
        landed = handle.read()
    if landed != text:
        raise ValueError("entry.txt on disk differs from the validated bio")


def main() -> int:
    bio = build_bio()
    validate_bio(bio)
    write_entry(bio)
    print(f"Wrote {len(bio)}-char bio to {OUT_PATH}")
    print(bio)
    return 0


if __name__ == "__main__":
    sys.exit(main())
