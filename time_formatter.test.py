import unittest
from extract_status import format_time

class TestTimeFormatter(unittest.TestCase):

    def test_format_time(self):
        test_cases = [
            (0, "0m"),
            (30, "30m"),
            (60, "1h"),
            (150, "2h 30m"),
            (1440, "1d"),
            (3720, "2d 14h"),
            (4380, "3d 1h"),
            (10080, "7d"),
            (10081, "7d 1m")
        ]

        for duration, expected_result in test_cases:
            result = format_time(duration)
            self.assertEqual(result, expected_result)

# Run the test
unittest.main()