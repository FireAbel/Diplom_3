import pytest
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from data import Urls

class TestPersonalAccount:
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_account_access(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page()
        assert driver.current_url == Urls.PROFILE

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_order_history_access(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page()
        account_page.click_order_history_link()
        assert driver.current_url == Urls.ORDER_HISTORY

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_logout(self, driver):
        account_page = AccountPage(driver)
        account_page.open_page()
        account_page.click_logout_button()
        assert driver.current_url == Urls.LOGIN 