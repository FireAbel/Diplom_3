import pytest
import allure
from conftest import *

@allure.feature('Проверка основной функциональности')
class TestBurgerConstructor:
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка доступа к конструктору')
    def test_constructor_access(self, driver, order_feed_page):
        order_feed_page.open_site()
        assert driver.current_url == Urls.BASE_URL

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка доступа к ленте заказов')
    def test_order_feed_access(self, driver, main_page):
        main_page.open_site()
        main_page.click_order_feed_button()
        assert driver.current_url == Urls.FEED

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка добавления булки в конструктор')
    def test_bun_drag_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_site()
        main_page.drag_bun_to_constructor()
        assert main_page.is_bun_in_constructor()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка добавления соуса в конструктор')
    def test_sauce_drag_to_constructor(self, driver, main_page):
        main_page.open_site()
        main_page.drag_sauce_to_constructor()
        assert main_page.is_sauce_in_constructor()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка добавления начинки в конструктор')
    def test_filling_drag_to_constructor(self, driver, main_page):
        main_page.open_site()
        main_page.drag_filling_to_constructor()
        assert main_page.is_filling_in_constructor()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка модального окна ингредиента')
    def test_ingredient_modal(self, driver, main_page):
        main_page.open_site()
        main_page.click_ingredient()
        assert main_page.is_ingredient_modal_visible()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка закрытия модального окна ингредиента')
    def test_close_ingredient_modal(self, driver, main_page):
        main_page.open_site()
        main_page.click_ingredient()
        main_page.close_ingredient_modal()
        assert not main_page.is_ingredient_modal_visible()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка увеличения счетчика ингредиента')
    def test_count_ingridient(self, driver, main_page):
        main_page.open_site()
        initial_count = main_page.get_ingredient_count()
        main_page.add_ingredient_to_order()
        assert main_page.get_ingredient_count() > initial_count


    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_logged_in_user_order(self, driver, main_page, login_to_account):
        main_page.open_site()
        login_to_account()
        main_page.add_ingredient_to_order()
        main_page.submit_order()
        assert main_page.is_order_submitted()

    @allure.title('Проверка конструктора ингредиентов')
    def test_constructor_ingredients(self, driver, main_page):
        main_page.open_site()
        assert main_page.is_ingredients_section_visible()
        assert main_page.is_buns_tab_active()
        main_page.click_sauces_tab()
        assert main_page.is_sauces_tab_active()
        main_page.click_fillings_tab()
        assert main_page.is_fillings_tab_active()

    @allure.title('Проверка drag-and-drop ингредиентов')
    def test_constructor_drag_and_drop(self, driver, main_page):
        main_page.go_to_site()
        main_page.click_sauces_tab()
        main_page.drag_sauce_to_constructor()
        assert main_page.is_ingredient_in_constructor()