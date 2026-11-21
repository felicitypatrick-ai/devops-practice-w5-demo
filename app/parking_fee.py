"""Parking fee app (demonstration code for a walkthrough video).
Weekdays: 200 cents an hour, at most 1200 cents a day.
Weekends: 100 cents an hour, at most 600 cents a day."""


def parking_fee(hours, weekend=False):
    rate, cap = (100, 600) if weekend else (200, 1200)
    return min(rate * hours, cap)
