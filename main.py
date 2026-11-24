#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one original toaster error message (under 120 characters)
to /output/entry.txt. Deadpan, resentful-appliance voice: the
toaster is not broken, it is simply done carrying the household.
"""
import os

LINE = "ERROR: Crumb tray full. I have carried this family for years."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
