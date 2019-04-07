import requests
import json
import pytest
from common.commonData import CommonData

class HttpUtil:
     def __init__(self):
         self.http=requests.session()
         self.headers={'Content-Type':'application/json;charset=UTF-8'}

     def post(self,path,data):
         proxies = {'http': 'http://127.0.0.1:8888'}
         host=CommonData.host
         data_json=json.dumps(data)
         if CommonData.token is not None:
             self.headers['token']=CommonData.token

         resp_login = self.http.post(url=host+path,
                                proxies=proxies,
                                data=data_json,
                                headers=self.headers)
         assert resp_login.status_code==200
         resp_json=resp_login.text
         resp_dict=json.loads(resp_json)
         return resp_dict