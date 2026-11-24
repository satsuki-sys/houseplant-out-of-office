#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (1-120 chars, UTF-8).
"""

import os

# Final entry (rewrite pass): the fern draft leaned on a stock office
# phrase ("I'll get back to you") and on the prompt's own example plant,
# so it risked reading as every other entry. This rewrite switches to a
# plant the brief never showcases — a succulent — and lets its own life
# drive the joke: it survives on nothing, so the sender's email can too.
# The payoff lands in the last few words.
ENTRY = "Out of office. I'm the succulent you forgot in February. I've lived on nothing since. Your email can do the same."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
