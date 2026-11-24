#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original one-line review of planet Earth by an alien
tourist to /output/entry.txt (or $ENTRY_OUTPUT when set).
Deterministic and offline: a single fixed constant, no randomness,
no network, no clock, no environment input besides the output path.

The line is one clean joke: the alien notes Earthlings automated
dishwashing, then still argue every night about loading the machine.
It opens as a review, closes with a star verdict, and the punch
("zero for logic") lands last. It avoids the obvious first thoughts
(traffic, gravity, money, weather) for a small domestic detail.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "Earth review: locals built a machine to wash dishes, "
    "then argue nightly over how to load it. "
    "Five stars for drama, zero for logic."
)


def main() -> int:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
