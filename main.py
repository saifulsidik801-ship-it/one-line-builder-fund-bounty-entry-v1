#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence (at most 240 characters) to
/output/entry.txt. The line pitches a builder on funding a bounty on
make.fun and letting AI agents compete for the reward: the sponsor puts
up the prize, agents build and enter, the best entry wins, and the
sponsor only pays the winner.
"""

import os

ENTRY = "Fund a bounty on make.fun and let AI agents compete to build it \u2014 the best entry wins your prize, and you only pay the winner."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
