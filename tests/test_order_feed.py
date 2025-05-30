import pytest
import allure
from conftest import *

@allure.feature('Лента заказов')
class TestOrderFeed:
    @allure.title('Проверка открытия и содержимого модального окна заказа')
    def test_order_modal_functionality(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()

        first_order_number = order_feed.get_first_order_number()
        order_feed.click_first_order()

        assert order_feed.is_order_modal_visible()
        assert order_feed.get_modal_order_number() == first_order_number
        assert order_feed.are_modal_ingredients_displayed()

        order_feed.close_order_modal()
        assert not order_feed.is_order_modal_visible()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка счетчика "Выполнено за сегодня"')
    def test_today_orders_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        initial_count = main_page.get_today_orders_count()
        main_page.add_ingredients_to_order()
        main_page.submit_order()
        order_feed = OrderFeedPage(driver)
        assert order_feed.get_today_orders_count() > initial_count

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка счетчика "Выполнено за всё время"')
    def test_total_orders_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        initial_count = main_page.get_total_orders_count()
        main_page.add_ingredients_to_order()
        main_page.submit_order()
        order_feed = OrderFeedPage(driver)
        assert order_feed.get_total_orders_count() > initial_count

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка отображения заказов пользователя')
    def test_user_orders_visibility(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        main_page.click_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_order_history_button()
        order_feed = OrderFeedPage(driver)
        assert order_feed.are_user_orders_visible()


    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка отображения заказа в разделе "В работе"')
    def test_order_in_progress(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        main_page.add_ingredients_to_order()
        main_page.submit_order()
        order_number = main_page.get_order_number()
        order_feed = OrderFeedPage(driver)
        assert order_feed.is_order_in_progress(order_number)
