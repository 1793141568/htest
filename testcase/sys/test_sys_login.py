# import pytest
# import requests
# from  common.commonData import CommonData
# from conftest import http
# class Test_Login():
#     def test_login_success(self):
#         path = '/sys/login'
#         data={'userName':CommonData.mobile,'password':CommonData.password}
#         resp=http.post(path,data)
#         assert resp['code']==200
#         assert resp['msg']=='操作成功'
#         assert resp['object']['userId']==154
#         print(resp)
#     def test_login_fail(self):
#         path = '/sys/login'
#         data = {'userName': CommonData.mobile, 'password':'1234567'}
#         resp = http.post(path, data)
#         assert resp['code'] == 410
#         assert resp['msg'] == '用户名或密码错误'
#         print(resp)
#     def test_login_fail1(self):
#         path = '/sys/login'
#         data = {'userName':'', 'password':CommonData.password}
#         resp = http.post(path, data)
#         assert resp['code'] == 301
#         assert resp['msg'] == '用户不存在'
#         print(resp)
#
#     def test_login_fail2(self):
#         path = '/sys/login'
#         data = {'password': CommonData.password}
#         resp = http.post(path, data)
#         assert resp['code'] == 301
#         assert resp['msg'] == '用户不存在'
#         print(resp)
#     def test_login_fail3(self):
#         path = '/sys/login'
#         data = {}
#         resp = http.post(path, data)
#         assert resp['code'] == 301
#         assert resp['msg'] == '用户不存在'
#         print(resp)
#     def test_login_fail4(self):
#         path = '/sys/login'
#         data = {'userName':'123456789123456', 'password':CommonData.password}
#         resp = http.post(path, data)
#         assert resp['code'] == 301
#         assert resp['msg'] == '用户不存在'
#         print(resp)