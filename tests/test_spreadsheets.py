import unittest
from spreadsheets import GoogleSpreadSheets


class GoogleSpreadSheetsTestCase(unittest.TestCase):

    def setUp(self):
        self.instance = GoogleSpreadSheets()


    def test_can_create_file(self):
        filename = 'Filename1'
        result = self.create_file(filename)
        self.assertIsNotNone(result.title, filename)

    def create_file(self, filename):
        return self.instance.create(filename)

    def test_can_write_to_file(self):
        filename = 'Filename2'
        username = 'gofaniyi'
        followers_count = 2000
        data={'Profile name' : username, 'Number of followers' : followers_count}
        self.instance.write(filename=filename, data=data)
