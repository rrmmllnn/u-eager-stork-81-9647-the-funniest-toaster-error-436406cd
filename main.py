#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one original toaster error message (under 120 characters)
to /output/entry.txt. Deadpan, resentful-appliance voice: the
toaster is not broken, it is simply done carrying the household.
"""
import os
import sys

LINE = "ERROR: Crumb tray at capacity. I am not a landfill with a heating element."


def main():
    if not LINE.strip() or "\n" in LINE or len(LINE) > 120:
        sys.exit("entry line must be one non-blank line of 1-120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
