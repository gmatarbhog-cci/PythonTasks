import openpyxl

class ExcelFile():
    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.Workbook()
        self.workbook.save(filename)
        self.active_sheet = self.workbook.active

    def find_in_cell(self):
        print('find in cell')

    def read_cell(self):
        print('reading cell {}'.format(self.active_sheet['A4'].value))

    def read_block_cells(self):
        print('reading cell {}'.format(self.active_sheet['A4':'A5'].value))

    def update_cell(self):
        self.active_sheet['A4'].value = 'hello'
        self.workbook.save('sample.xlsx')


excel = ExcelFile('sample.xlsx')
excel.update_cell()
excel.read_cell()
excel.read_block_cells()