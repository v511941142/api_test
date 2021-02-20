from data.get_data import GetData
from base.run_method import RunMethod

class RunMain:
    def __init__(self):
        self.data = GetData()
        self.run = RunMethod()

    def run_test(self):
        t = self.data.get_case_count()
        for i in range(1,t):
            if self.data.get_isRun(i) == 'yes':
                method = self.data.get_method(i)
                url = self.data.get_url(i)
                data = self.data.get_requests_data(i)
                header = self.data.get_header(i)
                res = self.run.run_method(method,url,data,header)
                except_data = self.data.get_except_data(i)
                result = 'fail'
                if except_data in res:
                    result = 'pass'
                self.data.write_result(i,result)





if __name__ == '__main__':
    RunMain().run_test()