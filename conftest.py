import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commonData import CommonData


http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path="/sys/login"
    data={'userName':CommonData.mobile,'password':CommonData.password}
    resp_login=http.post(path,data)
    CommonData.token=resp_login['object']['token']
    print("登录成功")
    yield
    path="/sys/logout"
    data ={'token':CommonData.token}
    resp_logout = http.post(path, data)
    print(resp_logout)
    print("退出登录")