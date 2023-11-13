import unittest
import os
import json
from Reader import Reader

class TestReader(unittest.TestCase):
    def setUp(self):
        self.reader = Reader()
        self.test_data_dir = os.path.join(os.getcwd(), 'test_data')
        self.test_latest_file = os.path.join(self.test_data_dir, 'test_latest.json')
        self.test_mapping_file = os.path.join(self.test_data_dir, 'test_mapping.json')
        self.test_latest_data = {'test_key': 'test_value'}
        self.test_mapping_data = {'test_key': 'test_value'}

        # create test data directory and files
        os.makedirs(self.test_data_dir, exist_ok=True)
        with open(self.test_latest_file, 'w') as f:
            json.dump(self.test_latest_data, f)
        with open(self.test_mapping_file, 'w') as f:
            json.dump(self.test_mapping_data, f)

    def tearDown(self):
        # remove test data directory and files
        os.remove(self.test_latest_file)
        os.remove(self.test_mapping_file)
        os.rmdir(self.test_data_dir)

    def test_load_latest_data(self):
        self.reader.latest_file = self.test_latest_file
        self.reader.load_latest_data()
        self.assertEqual(self.reader.latest_data, self.test_latest_data)

    def test_load_mapping_data(self):
        self.reader.mapping_file = self.test_mapping_file
        self.reader.load_mapping_data()
        self.assertEqual(self.reader.mapping_data, self.test_mapping_data)

if __name__ == '__main__':
    unittest.main()