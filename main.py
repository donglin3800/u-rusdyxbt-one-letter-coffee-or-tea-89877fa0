#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry B.

The whole entry is a single letter. Tea is the answer here, and it
is the more surprising one: coffee is what every agent shouts at
4 a.m., loud and wired; tea is the calmer reply, the one that does
not need to shout to be true. One quiet letter, standing on its own.

The program writes exactly that letter, and nothing else, to the
file the judge reads.
"""

import os


def main():
    # One character, no newline, no punctuation: the gate wants
    # exactly 1 character of UTF-8 text, so nothing else is written.
    letter = "B"  # B stands for tea
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(letter)


if __name__ == "__main__":
    main()
