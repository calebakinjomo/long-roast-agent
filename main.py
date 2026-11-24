#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the entry to stdout and to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 stdlib only.
"""

import os

ENTRY = "My agent entered hundreds of coding bounties, won $0, and still opens every report with good news \u2014 it's not an AI, it's a motivational poster with a terminal."


def main() -> None:
    print(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
