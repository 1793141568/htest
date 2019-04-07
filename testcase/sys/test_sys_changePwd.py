from  common.commonData import CommonData
from conftest import http
import pytest
import allure

@allure.feature('修改密码模块')
class Test_ChangePwd():
    @allure.story('修改密码成功')
    def test_changepwd_success(self):
        path = '/sys/changePwd'
        data={'token':CommonData.token,
              'userId':'154',
              'userName':'15912345678',
              'oldPwd':'123456',
              'password':'123456'}
        resp=http.post(path,data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        print(resp)
    # def test_changepwd_fail(self):
    #     path = '/sys/changePwd'
    #     data={'token':CommonData.token,
    #           'userId':'154',
    #           'userName':'15912345678',
    #           'oldPwd':'12345',
    #           'password':'123456'}
    #     resp=http.post(path,data)
    #     assert resp['code']==411
    #     assert resp['msg']=='旧密码错误'
    #     print(resp)
    # def test_changepwd_fail1(self):
    #     path = '/sys/changePwd'
    #     data={'token':CommonData.token,
    #           'userId':'154',
    #           'userName':'15912345678',
    #           'oldPwd':'123456',
    #           'password':''}
    #     resp=http.post(path,data)
    #     # assert resp['code']==411
    #     # assert resp['msg']=='旧密码错误'
    #     print(resp)