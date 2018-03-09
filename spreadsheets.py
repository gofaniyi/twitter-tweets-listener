import pygsheets


def is_empty(data):
    valid_count = 0
    for element in data:
        if element and element != ['']:
            valid_count += 1
    return valid_count == 0

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

    def read(self, worksheet):
        return worksheet.get_all_values(returnas='matrix')


    def delete(self, worksheet):
        del_worksheet(worksheet)

    def write(self, spreadsheet=None, filename=None, payload=None):
        if not spreadsheet:
            try:
                spreadsheet = self.open(filename)
            except pygsheets.SpreadsheetNotFound:
                spreadsheet = self.create(filename)

        wks = spreadsheet.sheet1
        data = self.read(wks)

        index = len(data)

        if is_empty(data):
            wks.update_cell('A1', 'Profile name')
            wks.update_cell('B1', 'Number of followers')

        index += 1

        # Update a cell with value (just to let him know values is updated ;) )
        wks.update_cell(f'A{index}', payload['Profile name'])
        wks.update_cell(f'B{index}', payload['Number of followers'])
        return wks
