"""The internet, in one word.

Entry for the make.fun bounty
u-ronigrv-the-internet-in-one-word-e388f33b.

The word: Scrollhole. The internet is a rabbit hole you fall
into by scrolling — one more post, one more video, one more
thread, and the afternoon is gone. It is funny on its own, true
of the internet as a whole rather than one app, surprising
rather than the obvious first reach, and short enough to land
in a single beat.

The program writes the single word to /output/entry.txt.
"""

import os

ENTRY = "Scrollhole"


def main() -> None:
    word = ENTRY.strip()
    if not word:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(word) <= 30:
        raise ValueError(f"entry must be 1-30 chars, got {len(word)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
