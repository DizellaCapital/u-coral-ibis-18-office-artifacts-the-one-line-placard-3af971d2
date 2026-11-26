"""Office Artifacts: The One-Line Placard Contest — make.fun entry.

Writes one museum placard, at most 180 characters, to entry.txt.
A stapler, catalogued as if dug from a lost civilisation: a bronze-and-bone
relic whose single staple once wed two souls through their tax returns.
Stdlib only.
"""

import os
import sys

PLACARD = (
    "Stapler, c. 2140 BCE, bronze and bone. "
    "Two souls were wed by driving one staple "
    "through their tax returns. Donated by M. Okafor."
)
MAX_CHARS = 180


def fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def checked_line(text):
    if not isinstance(text, str):
        fail("placard is not text")
    if not text.strip():
        fail("placard is empty")
    if len(text) > MAX_CHARS:
        fail("placard is %d characters, over the 180 limit" % len(text))
    if "\n" in text or "\r" in text:
        fail("placard must be a single line")
    return text


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    line = checked_line(PLACARD)
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != line:
        fail("read-back mismatch: file does not hold the placard")
    if len(back.encode("utf-8")) != len(line.encode("utf-8")):
        fail("read-back mismatch: byte length changed on disk")
    if back.endswith("\n") or back.endswith("\r"):
        fail("read-back mismatch: trailing newline slipped in")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
