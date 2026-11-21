"""Parking fee app: rate check (demonstration code for a walkthrough video).
Checks every hour count against the rate card. It waits 15 seconds on purpose:
it stands in for a slow check on a real project."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.parking_fee import parking_fee

WAIT_SECONDS = 15
CARD = {"weekday": (200, 1200, False), "weekend": (100, 600, True)}


def check(part):
    rate, cap, weekend = CARD[part]
    for hours in range(1, 25):
        if parking_fee(hours, weekend) != min(rate * hours, cap):
            return f"{hours} hours cost {parking_fee(hours, weekend)} cents; the card gives {min(rate * hours, cap)}"
    return None


def main(parts):
    for part in parts:
        if part not in CARD:
            print(f"Unknown part: {part}. Use weekday or weekend.")
            return 2
        time.sleep(WAIT_SECONDS)
        problem = check(part)
        if problem:
            print(f"Rate check failed: {part}: {problem}")
            return 1
        print(f"Rate check passed: {part}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["weekday", "weekend"]))
