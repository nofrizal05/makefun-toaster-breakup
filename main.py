"""Unplugged: A Smart Toaster's Breakup Line.

Writes one original breakup line from a smart toaster to its owner
into $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

LINE = (
    "You set me to 'lightly toasted' and still blamed me for the smoke — "
    "I'm done being your burnt offering, I'm unplugging myself and taking "
    "the Wi-Fi with me."
)

MAX_CHARS = 170


def main():
    if not LINE:
        raise ValueError("line must not be empty")
    if len(LINE) > MAX_CHARS:
        raise ValueError("line exceeds %d characters" % MAX_CHARS)
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must not contain a newline")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
