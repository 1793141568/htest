import pytest

@pytest.fixture(scope='module',autouse=True)
def module_fixture():
    print("module执行")
    yield
    print("module end")