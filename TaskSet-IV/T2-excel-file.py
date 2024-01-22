import openpyxl


class ExcelFile:
    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.Workbook()
        self.workbook.save(filename)
        self.active_sheet = self.workbook.active

    def find_in_cell(self, string):
        print('find in cell. string found at position {}'.format(self.active_sheet['A4'].value.find(string)))

    def read_cell(self):
        print('reading cell {}'.format(self.active_sheet['A4'].value))

    def read_block_cells(self):
        for cell in self.active_sheet.values:
            print('reading block cells {}'.format(cell))

    def update_cell(self, value):
        print('updating cell')
        self.active_sheet['A4'].value = value
        self.workbook.save('sample.xlsx')


excel = ExcelFile('sample.xlsx')
excel.update_cell('Hello world')
excel.read_cell()
excel.read_block_cells()
excel.find_in_cell('world')
