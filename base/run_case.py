from datetime import datetime
import unittest
import mock
import HTMLTestRunner
from base.run_method import RunMethod
from base.run_mock import RunMock


class TestCase(unittest.TestCase):
    def setUp(self):
        print('test start')
        self.run = RunMethod()
        self.mock = RunMock()

    def tearDown(self):
        print('test end')

    def test_01(self):
        url = 'http://616856.18crm.com/xls2/common/appcrmserver.ashx'
        data = {'method': 'appcard_carddetail_getinfobyname', 'name': 'tc05'}
        mock_res = {'method': 'this is mock response'}
        # self.run.send_requests = mock.Mock(return_value = mock_res)
        res = self.mock.run_mock(self.run.run_method, 'POST', url, data, mock_res)
        print(res)

    # def test_01(self):
    #     print('这是test1')
    #     r = self.run.send_requests('POST', url, data)
    #     self.assertEqual(r['message'], '获取成功', '测试1不通过')
    #     self.assertEqual(r['code'], '200', '测试1不通过')
    #     self.assertEqual(r['data']['list'][0]['carddetail_id'], 247, '测试1不通过')
    #     self.assertEqual(r['data']['list'][0]['consumename'], '药浴', '测试1不通过')
    #     self.assertEqual(r['data']['list'][0]['currentcount'], 1.0, '测试1不通过')


if __name__ == '__main__':
    unittest.main()
    # t = datetime.now().strftime('%Y-%m-%d-%Hh%Mm%Ss')
    # path = '../report/report-%s.html' % t
    # fp = open(path, 'wb')
    # suite = unittest.TestSuite()
    # suite.addTest(TestCase('test_01'))
    # suite.addTest(TestCase('test_02'))
    # suite.addTest(TestCase('test_03'))
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试日期:' + t, description='这是描述')
    # runner.run(suite)
