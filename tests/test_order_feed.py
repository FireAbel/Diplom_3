import pytest
import allure
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import Urls, UserTestData

@allure.feature('Лента заказов')
class TestOrderFeed:
    
    @allure.title('Проверка отображения ленты заказов')
    def test_order_feed_display(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        
        assert order_feed.is_order_feed_visible()
        assert order_feed.are_orders_displayed()
        assert order_feed.is_order_statistics_visible()
    
    @allure.title('Проверка открытия и содержимого модального окна заказа')
    def test_order_modal_functionality(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        
        # Открытие модального окна
        first_order_number = order_feed.get_first_order_number()
        order_feed.click_first_order()
        
        # Проверка содержимого модального окна
        assert order_feed.is_order_modal_visible()
        assert order_feed.get_modal_order_number() == first_order_number
        assert order_feed.are_modal_ingredients_displayed()
        
        # Закрытие модального окна
        order_feed.close_order_modal()
        assert not order_feed.is_order_modal_visible()
    
    @allure.title('Проверка корректности отображения счётчиков заказов')
    def test_order_counters_display(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        
        # Проверка счётчика "Выполнено за все время"
        assert order_feed.is_total_orders_counter_visible()
        total_count = order_feed.get_total_orders_count()
        assert isinstance(total_count, int) and total_count >= 0
        
        # Проверка счётчика "Выполнено за сегодня"
        assert order_feed.is_today_orders_counter_visible()
        today_count = order_feed.get_today_orders_count()
        assert isinstance(today_count, int) and today_count >= 0
        
        # Проверка списка "В работе"
        assert order_feed.is_in_progress_section_visible()
        in_progress_orders = order_feed.get_in_progress_orders()
        assert isinstance(in_progress_orders, list)

    @allure.title('Проверка отображения заказов в истории')
    def test_orders_displayed_in_history(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        assert order_feed.are_user_orders_visible()
        
    @allure.title('Проверка увеличения счетчика "Выполнено за все время"')
    def test_total_orders_counter_increases(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        initial_count = order_feed.get_total_orders_count()
        
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        
        main_page = MainPage(driver)
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        main_page.wait_for_order_success()
        
        order_feed.open_page()
        final_count = order_feed.get_total_orders_count()
        assert final_count > initial_count
        
    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня"')
    def test_today_orders_counter_increases(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        initial_count = order_feed.get_today_orders_count()
        
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        
        main_page = MainPage(driver)
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        main_page.wait_for_order_success()
        
        order_feed.open_page()
        final_count = order_feed.get_today_orders_count()
        assert final_count > initial_count
        
    @allure.title('Проверка появления номера заказа в разделе "В работе"')
    def test_order_appears_in_progress(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login_user(UserTestData.TEST_USER_EMAIL, UserTestData.TEST_USER_PASSWORD)
        
        main_page = MainPage(driver)
        main_page.add_ingredients_to_order()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        assert order_feed.is_order_in_progress(order_number)

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_order_modal(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        order_feed.click_first_order()
        assert order_feed.is_order_modal_visible()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_orders_in_history(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        assert order_feed.are_orders_displayed_in_history()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_total_orders_counter_increase(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        initial_count = order_feed.get_total_orders_count()
        order_feed.create_new_order()
        assert order_feed.get_total_orders_count() > initial_count

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_today_orders_counter_increase(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        initial_count = order_feed.get_today_orders_count()
        order_feed.create_new_order()
        assert order_feed.get_today_orders_count() > initial_count

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_order_appears_in_progress(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        order_feed.create_new_order()
        assert order_feed.is_order_in_progress()