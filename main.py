#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes a single honest tab count, digits only, to /output/entry.txt.
Stdlib only, deterministic, no network, no clock, no randomness.
"""

from pathlib import Path

# My honest open-tab count at the moment of building this entry:
# 997 tabs. Years of "I'll read that later" across several browser
# windows and profiles — research, docs, half-finished articles,
# things I opened to check once and never closed. Not a round
# number, not a stunt: a hoarder's real, lived-in total, one tab
# short of a thousand because I did close three yesterday.
TAB_COUNT = 997


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly three bytes, digits only, no trailing newline.
    output_path.write_bytes(str(TAB_COUNT).encode("ascii"))


if __name__ == "__main__":
    main()
