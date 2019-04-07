import pytest
@pytest.fixture()
def my_fixtures():
    print("用户初始化")
    yield
    print("用户恢复")
# def test_first():
#     print('用户：我的第一个pytest测试')
#     #assert 1!=2
# @pytest.mark.debug
# @pytest.mark.usefixtures("my_fixtures")
# def test_second():
#     print('用户：我的第二个pytest测试')
#     #assert 2==2
# @pytest.mark.info
# @pytest.mark.usefixtures("my_fixtures")
# def test_three():
#     print('用户：我的第三个pytest测试')
#     #assert 'a' in 'ab'