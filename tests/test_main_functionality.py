import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from data import Urls

class TestMainFunctionality:
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_constructor_access(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        assert driver.current_url == Urls.BASE_URL

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_order_feed_access(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.open_page()
        assert driver.current_url == Urls.ORDER_FEED

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_ingredient()
        assert main_page.is_ingredient_modal_visible()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_ingredient()
        main_page.close_ingredient_modal()
        assert not main_page.is_ingredient_modal_visible()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        initial_count = main_page.get_ingredient_count()
        main_page.add_ingredient_to_order()
        assert main_page.get_ingredient_count() > initial_count

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_logged_in_user_order(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.login_user('test@example.com', 'password')
        main_page.add_ingredient_to_order()
        main_page.submit_order()
        assert main_page.is_order_submitted() 