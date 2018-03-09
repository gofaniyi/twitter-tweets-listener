import unittest
from datetime import datetime
import json
from spreadsheets import GoogleSpreadSheets


class GoogleSpreadSheetsTestCase(unittest.TestCase):

    def setUp(self):
        self.instance = GoogleSpreadSheets()


    def test_can_create_file(self):
        filename = f'Filename New {datetime.now().strftime("%Y%m%d%H%M%s")}'
        result = self.create_file(filename)
        self.assertIsNotNone(result.title, filename)

    def create_file(self, filename):
        return self.instance.create(filename)

    def read_file(self, worksheet):
        return self.instance.read(worksheet)

    def test_can_write_to_file(self):
        filename = f'Filename New {datetime.now().strftime("%Y%m%d%H%M%s")}'
        username = 'gofaniyi'
        followers_count = 2000
        data={'Profile name' : username, 'Number of followers' : followers_count}
        worksheet = self.instance.write(filename=filename, payload=data)
        self.assertIsNotNone(worksheet)
        read_data = self.read_file(worksheet)
        self.assertIn(username, json.dumps(read_data))
