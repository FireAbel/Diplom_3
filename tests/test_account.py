import pytest
import allure
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from data import Urls

@allure.feature('Личный кабинет')
class TestAccount:
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Переход в личный кабинет по клику на "Личный кабинет"')
    def test_account_access_after_login(self, driver, login_to_account):
        account_page = AccountPage(driver)
        assert account_page.get_current_url() == Urls.BASE_URL, "URL не соответствует базовому URL"

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Переход в раздел "История заказов"')
    def test_order_history_access(self, driver, login_to_account):
        account_page = AccountPage(driver)
        account_page.driver.get(Urls.PROFILE)
        account_page.click_order_history_link()
        assert account_page.get_current_url() == Urls.ORDER_HISTORY, "URL не соответствует странице истории заказов"

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Выход из аккаунта')
    def test_logout_and_redirect(self, driver, login_to_account):
        account_page = AccountPage(driver)
        account_page.click_logout_button()
        assert account_page.get_current_url() == Urls.LOGIN, "URL не соответствует странице логина"