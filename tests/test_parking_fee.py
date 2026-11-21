import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.parking_fee import parking_fee


class ParkingFeeTest(unittest.TestCase):
    def test_two_weekday_hours(self):
        self.assertEqual(parking_fee(2), 400)

    def test_weekday_cap(self):
        self.assertEqual(parking_fee(9), 1200)

    def test_weekend_cap(self):
        self.assertEqual(parking_fee(9, weekend=True), 600)


if __name__ == "__main__":
    unittest.main()
