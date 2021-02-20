from util.operate_excel import OperateExcel
from util.operate_json import OperateJson
from data.data_config import GlobalVar


class GetData:
    def __init__(self):
        self.op_excel = OperateExcel()
        self.op_json = OperateJson()
        self.data = GlobalVar()

    def get_case_count(self):
        return self.op_excel.get_lines()

    def get_isRun(self, row):
        col = self.data.isRun
        return self.op_excel.get_value(row, col)

    def get_url(self, row):
        col = self.data.url
        return self.op_excel.get_value(row, col)

    def get_method(self, row):
        col = self.data.method
        return self.op_excel.get_value(row, col)

    def get_header(self, row):
        col = self.data.header
        header = None
        if self.op_excel.get_value(row, col):
            header = self.op_json.get_value(self.op_excel.get_value(row, col))
        return header

    def get_requests_data(self, row):
        col = self.data.requests_data
        return self.op_json.get_value(self.op_excel.get_value(row, col))

    def get_except_data(self, row):
        col = self.data.expect_data
        return self.op_excel.get_value(row, col)

    def write_result(self, row, value):
        col = self.data.result
        self.op_excel.write_value(row, col, value)


if __name__ == '__main__':
    g = GetData()
    r = g.get_except_data(1)
    print(type(r))
    g.write_result(2,'wt')
