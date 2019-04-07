# import pytest
# @pytest.fixture()
# def my_fixtures():
#     print("登录初始化")
#     yield
#     print("login end")
# @pytest.mark.debug
# def test_first():
#     print('登录：我的第一个pytest测试')
#     #assert 1!=2
# @pytest.mark.usefixtures("my_fixtures")
# def test_second():
#     print('登录：我的第二个pytest测试')
#     #assert 2==2
# @pytest.mark.usefixtures("my_fixtures")
# def test_three():
#     print('登录：我的第三个pytest测试')
#     #assert 'a' in 'ab'