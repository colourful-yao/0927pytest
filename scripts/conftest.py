import pytest
from common.base import open_app
from page.login_page import LoginPage
@pytest.fixture()
def driver_init(request):
    driver = open_app()
    login = LoginPage(driver)
    login.login("yuanma","123456")
    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver
