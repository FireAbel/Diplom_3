import allure
import pytest
from conftest import *
from urls import Urls
from locators.main_locators import MainPageLocators


@allure.feature('Проверка основной функциональности')
class TestBurgerConstructor:
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка доступа к конструктору')
    def test_constructor_access(self, driver, order_feed_page):
        order_feed_page.open_site()
        order_feed_page.click_on_constructor_text()
        assert driver.current_url == Urls.BASE_URL

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка доступа к ленте заказов')
    def test_order_feed_access(self, driver, main_page):
        main_page.open_site()
        main_page.click_order_feed_button()
        assert driver.current_url == Urls.FEED

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка увеличения счетчика ингредиента')
    def test_count_ingredient(self, driver, main_page):
        main_page.open_site()
        main_page.drag_and_drop_ingredient(MainPageLocators.BUN_CARD, MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.drag_and_drop_ingredient(MainPageLocators.SAUCE_CARD, MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.drag_and_drop_ingredient(MainPageLocators.FILLING_CARD, MainPageLocators.CONSTRUCTOR_BURGER)
        assert main_page.get_bun_counter() == '2'
        assert main_page.get_sauce_counter() == '1'
        assert main_page.get_filling_counter() == '1'

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_logged_in_user_order(self, driver, main_page, login_to_account):
        main_page.open_site()
        main_page.drag_and_drop_ingredient(MainPageLocators.BUN_CARD, MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.create_order()
        main_page.wait_for_order_number_visibility()
        assert main_page.is_order_identified_visible()

    @allure.title('Проверка открытия модального окна при клике на ингредиент')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_ingredient_modal(self, driver, main_page):
        main_page.open_site()
        main_page.click_bun_card()
        assert main_page.check_visible_bun_card()

    @allure.title('Проверка закрытия модального окна при клике на кнопку закрытия модального окна')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_close_ingredient_modal(self, driver, main_page):
        main_page.open_site()
        main_page.click_bun_card()
        main_page.close_bun_card()
        assert main_page.check_invisible_bun_card()