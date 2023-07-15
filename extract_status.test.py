import unittest
from extract_status import parse_json

class TestParseJson(unittest.TestCase):
    def test_parse_json(self):
        with open('./test_data/test-response.json', 'r') as file:
            json_data = file.read()

        expected_result = {
            "TP-1": {
                "Backlog": "1h 33m",
                "Selected for Development": "0m",
                "In Progress": "3h 15m",
                "Done": "0m"
            }
        }

        result = parse_json(json_data)
        self.assertEqual(result, expected_result)

# Run the test
unittest.main()