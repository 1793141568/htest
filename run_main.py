import pytest



if __name__ == '__main__':
    pytest.main(['-s','--alluredir','./report/xml'])

    # allure generate report/xml/-o report/html -clean