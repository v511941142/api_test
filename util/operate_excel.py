import xlrd
import xlwt
from xlutils.copy import copy


class OperateExcel:
    def __init__(self, file_path='../config/interface.xlsx', sheet_index=0):
        self.file_path = file_path
        self.sheet_index = sheet_index
        self.table = self.__get_table()

    def __get_table(self):
        workbook = xlrd.open_workbook(self.file_path)
        return workbook.sheets()[self.sheet_index]

    def get_value(self, row, col):
        return self.table.cell_value(row, col)

    def get_lines(self):
        return self.table.nrows

    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_path)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_path)


if __name__ == '__main__':
    op_excel = OperateExcel()
    result = op_excel.get_value(1, 11)
    op_excel.write_value(2, 11, 'abc')
