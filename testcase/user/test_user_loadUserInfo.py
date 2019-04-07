import pytest
import requests
from  common.commonData import CommonData
from conftest import http

class Test_LoadUserInfo():
    def test_loaduserinfo_success(self):
        path = '/user/saveOrUpdateUser'
        data={'nickName':'尚华杰23333',
              'userName':'13533333343',
              'telNo':'','email':'','address':'','roleIds':'','regionId':1,'regionLevel':1}
        resp=http.post(path,data)
        assert resp['code']==401
        assert resp['msg']=='无权限访问'
        print(resp)
    def test_login(self):
        path = "/sys/login"
        data = {'userName':'13533333343' , 'password': '123456'}
        resp_login = http.post(path, data)
        CommonData.token = resp_login['object']['token']
        id=resp_login['object']['userId']
        print(id)
        return id
    def test_loadUserList(self):
        path = '/user/loadUserList'
        data = {'pageCurrent':1,'pageSize':1,'nickName':'','userName':'','regionId':1}
        resp = http.post(path, data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        assert resp['object']['list'][0]['id'] == self.test_login()
        assert resp['object']['list'][0]['nickName']== '尚华杰23333'
        print(resp)
        return resp['object']['list'][0]['id']

    def test_loadUserInfo(self):
        path = '/user/loadUserInfo'
        data = {'id':self.test_loadUserList()}
        resp = http.post(path, data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print(resp)