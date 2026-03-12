import pytest
import allure
from conftest import *
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_locators import MainPageLocators


@allure.feature('Личный кабинет')
class TestAccount:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка перехода в личный кабинет')
    def test_account_access(self, driver, login_to_account, main_page, account_page):
        main_page.wait_for_button_active(MainPageLocators.ACCOUNT_BUTTON)
        main_page.click_account_button()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.PROFILE)) # Добавлено ожидание смены URL
        account_page.wait_for_page_load()
        assert main_page.get_current_site() == Urls.PROFILE

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка перехода в историю заказов через кнопку')
    def test_go_to_order_history(self, driver, main_page, login_to_account, account_page):
        main_page.wait_for_button_active(MainPageLocators.ACCOUNT_BUTTON)
        main_page.click_account_button()
        account_page.click_order_history()
        assert account_page.get_current_site() == Urls.ORDER_HISTORY

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка выхода из аккаунта через кнопку Выйти')
    def test_logout(self, driver, main_page, login_to_account, account_page, login_page):
        main_page.wait_for_button_active(MainPageLocators.ACCOUNT_BUTTON)
        main_page.click_account_button()
        account_page.click_logout_button()
        assert driver.current_url == Urls.LOGIN