# import pytest
# import requests
# from  common.commonData import CommonData
# from conftest import http
# class Test_GetUserInfo():
#     def test_getuserinfo_success(self):
#         path = '/sys/getUserInfo'
#         data={'token':CommonData.token}
#         resp=http.post(path,data)
#         assert resp['code']==200
#         assert resp['msg']=='操作成功'
#         print(resp)