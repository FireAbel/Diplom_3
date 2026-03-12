import pytest
import allure
from conftest import *
from locators.main_locators import MainPageLocators


@allure.feature('Лента заказов')
class TestOrderFeed:
    @allure.title('Проверка открытия модального окна заказа')
    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_open_order_modal_functionality(self, driver, order_feed_page):
        order_feed_page.open_site()
        order_feed_page.click_first_order()
        assert order_feed_page.is_order_modal_visible()

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @pytest.mark.parametrize('counter_type', ['today', 'total'])
    @allure.title('Проверка увеличения счетчиков заказов')
    def test_order_counters_increase(self, driver, login_to_account, main_page, order_feed_page, counter_type):
        order_feed_page.open_site()
        if counter_type == 'today':
            count_before = int(order_feed_page.get_today_orders())
            counter_name = "Выполнено за сегодня"
        else:  # 'total'
            count_before = int(order_feed_page.get_total_orders())
            counter_name = "Выполнено за все время"
        main_page.open_site()
        main_page.drag_and_drop_ingredient(MainPageLocators.BUN_CARD, MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.create_order()
        main_page.wait_for_order_number_visibility()
        main_page.close_modal_order()
        order_feed_page.open_site()
        if counter_type == 'today':
            count_after = int(order_feed_page.get_today_orders())
        else:  # 'total'
            count_after = int(order_feed_page.get_total_orders())

        allure.attach(f"Значение '{counter_name}' после создания заказа: {count_after}", name="Счетчик после")
        assert count_after > count_before

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка отображения заказа пользователя в общей ленте заказов')
    def test_user_order_appears_in_feed(self, driver, login_to_account, main_page, order_feed_page):
        main_page.open_site()
        main_page.drag_and_drop_ingredient(MainPageLocators.BUN_CARD, MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.create_order()
        main_page.wait_for_order_number_visibility()
        order_id = main_page.get_order_id()
        main_page.close_modal_order()
        if order_id.startswith('#'):
            clean_order_id = order_id[1:]
        else:
            clean_order_id = order_id
        order_feed_page.open_site()
        assert order_feed_page.is_order_visible_in_feed(clean_order_id)

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка отображения заказа в разделе "В работе"')
    def test_order_in_progress(self, driver, login_to_account, main_page, order_feed_page):
        main_page.open_site()
        main_page.drag_and_drop_ingredient(MainPageLocators.BUN_CARD, MainPageLocators.CONSTRUCTOR_BURGER)
        main_page.create_order()
        main_page.wait_for_order_number_visibility()
        order_id = main_page.get_order_id()
        main_page.close_modal_order()
        if order_id.startswith('#'):
            clean_order_id = order_id[1:]
        else:
            clean_order_id = order_id
        order_feed_page.open_site()
        assert order_feed_page.is_order_in_processing(clean_order_id)