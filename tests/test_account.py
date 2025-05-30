import pytest
import allure
from conftest import *
from urls import Urls

@allure.feature('Личный кабинет')
class TestAccount:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка перехода в личный кабинет')
    def test_account_access(self, driver, login_to_account, main_page):
        main_page.open_site()
        main_page.click_login_button()
        login_to_account()
        main_page.click_account_button()
        assert driver.current_url == Urls.PROFILE

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка перехода в историю заказов через кнопку')
    def test_go_to_order_history(self, driver, main_page, login_to_account, account_page):
        main_page.open_site()
        main_page.click_login_button()
        login_to_account()
        main_page.click_account_button()
        account_page.click_order_history()
        assert driver.current_url == Urls.ORDER_HISTORY

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка выхода из аккаунта через кнопку Выйти')
    def test_logout(self, driver, main_page, login_to_account, account_page):
        main_page.open_site()
        main_page.click_login_button()
        login_to_account()
        main_page.click_account_button()
        account_page.click_logout_button()
        assert driver.current_url == Urls.LOGIN

