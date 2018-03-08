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
        data = {'name' : 'gofaniyi', 'followers_count' : 2000}
        self.instance.write(filename=filename, data=data)
