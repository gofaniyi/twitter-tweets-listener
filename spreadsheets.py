import pygsheets

class GoogleSpreadSheets(object):

    def __init__(self):
        self.gc = pygsheets.authorize(outh_file='client_secret.json')


    def create(self, filename='New File'):
        # Create spreadsheet
        spreadsheet = self.gc.create(filename)
        return spreadsheet

    def open(self, filename):
        spreadsheet = None
        try:
            spreadsheet = self.gc.open(filename)
            return spreadsheet
        except pygsheets.SpreadsheetNotFound as e:
            raise e



    def write(self, spreadsheet=None, filename=None, data=None):
        if not spreadsheet:
            try:
                spreadsheet = self.open(filename)
            except pygsheets.SpreadsheetNotFound:
                spreadsheet = self.create(filename)

        wks = spreadsheet.sheet1
        # Update a cell with value (just to let him know values is updated ;) )
        wks.update_cell('A1', data['name'])
        wks.update_cell('B1', data['followers_count'])
