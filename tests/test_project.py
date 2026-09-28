import sys
import os

sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest

from file_handler import save_data, load_data


class TestFileHandler(unittest.TestCase):

    test_file = "test_data.json"

    def tearDown(self):
        file_path = os.path.join("data", self.test_file)
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_save_and_load_data(self):
        sample_data = [
            {"name": "Test Student", "value": 10}
        ]

        result = save_data(self.test_file, sample_data)

        self.assertTrue(result)
        self.assertEqual(load_data(self.test_file), sample_data)

    def test_load_missing_file(self):
        result = load_data("missing_test_file.json")

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()