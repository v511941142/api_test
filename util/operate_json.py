import json
import requests


class OperateJson:
    def __init__(self, file_path='../config/interface.json'):
        self.file_path = file_path
        self.json = self.__get_json()

    def __get_json(self):
        with open(self.file_path) as fp:
            return json.load(fp)

    def get_value(self, key):
        return self.json[key]


if __name__ == '__main__':
    op_json = OperateJson()
    r = op_json.get_value('case0001_requests_data')
    print(r)