import mock
import requests
import json


class RunMock:
    def run_mock(self, mock_method, requests_method, url, data, mock_res):
        mock_method = mock.Mock(return_value=mock_res)
        res = mock_method(requests_method, url, data)

        return res


if __name__ == '__main__':
    import requests

    url = 'http://www.18crm.com/xls2/common/appcrmserver.ashx'
    data = {'method': 'get_player', 'name': 'Curry'}
    mock_res = {"code": 400501, "message": "no found ad", "data": None}
    res = RunMock().run_mock(requests.post, 'POST', url, data, mock_res)
    print(res)
