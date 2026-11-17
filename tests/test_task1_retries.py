import unittest
from unittest import mock

from assistant import booking
from assistant.graph import ask


class Task1(unittest.TestCase):
    def run_counting(self, flight):
        calls = []
        real = booking.free_seats

        def counting(f):
            calls.append(f)
            return real(f)

        with mock.patch.object(booking, "free_seats", counting):
            return ask("Can the passenger take an earlier flight today?", flight), len(calls)

    def test_booking_down_gives_up_after_3_tries(self):
        result, calls = self.run_counting("UA900")
        self.assertGreaterEqual(calls, 2, "it should retry at least once")
        self.assertLessEqual(calls, 3, "it should try the booking system at most 3 times")
        self.assertIn("could not check seats", result["answer"])

    def test_booking_up_tries_once(self):
        result, calls = self.run_counting("UA100")
        self.assertEqual(calls, 1)
        self.assertIn("Free seats on that flight: 4", result["answer"])
