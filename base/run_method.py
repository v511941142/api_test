import requests
import json

class RunMethod:
    def __send_get(self, url, data, header=None):
        res = requests.get(url=url, params=data, headers=header)
        return res

    def __send_post(self, url, data, header=None):
        res = requests.post(url=url, data=data, headers=header)
        return res

    def run_method(self, method, url, data, header=None):
        if method == 'GET':
            res = self.__send_get(url, data)
        elif method == 'POST':
            res = self.__send_post(url, data)
        return res.text
        # return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)




if __name__ == '__main__':
    url = 'http://616856.18crm.com/xls2/common/appcrmserver.ashx'
    data = {"method": "appcard_cardmoney_getinfo", "cinfo": "{'fcm_areaname':'0.001','fcm_id':'0012101190011'}"}
    r = RunMethod().run_method('GET', url, data)
    print(r)
