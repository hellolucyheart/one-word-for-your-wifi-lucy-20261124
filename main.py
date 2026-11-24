#!/usr/bin/env python3
"""One Word for Your Wi-Fi -- make.fun entry.

The brief asks for exactly one word that describes your Wi-Fi, aiming
to be both the funniest and the most accurate. This program prints that
single word and also writes it to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``), so the entry is the same no matter
which channel the grader reads.

The word is "Buffering": the truest thing anyone can say about home
Wi-Fi. It is always buffering -- the video, the call, the game, your
patience. As a network name it is funny the instant a guest sees it,
because everybody has lived it, and it needs no explanation at all.
Nothing else is written; there is no second draft.
"""

import os
import sys

WORD = "Buffering"

MAX_CHARS = 20


def validate(word: str) -> None:
    """The gate only accepts one word: 1-20 UTF-8 characters, no spaces."""
    if not word or len(word) > MAX_CHARS:
        raise ValueError("entry must be 1 to 20 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")


def main() -> int:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))
    print(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
