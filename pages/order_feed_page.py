from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from data import Urls

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.FEED

    def open_page(self):
        self.open(self.url)
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(OrderFeedLocators.ORDER_DETAILS_MODAL, time=5)
        except:
            pass

    def click_first_order(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(OrderFeedLocators.ORDER_DETAILS_MODAL, time=5)
        except:
            pass
        self.find_clickable(OrderFeedLocators.FIRST_ORDER, time=10)
        self.click_element(OrderFeedLocators.FIRST_ORDER)

    def is_order_modal_opened(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL, time=10)

    def get_total_orders_count(self):
        return int(self.find_element(OrderFeedLocators.DONE_ALL_TIME_COUNTER, time=10).text)

    def get_today_orders_count(self):
        return int(self.find_element(OrderFeedLocators.DONE_TODAY_COUNTER, time=10).text)

    def is_order_in_progress(self, order_number):
        orders = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS, time=10)
        return any(order.text == str(order_number) for order in orders)

    def get_feed_title_text(self):
        return self.get_element_text(OrderFeedLocators.ORDER_FEED_TITLE)

    def click_any_order_card(self):
        try:
            # Ждем исчезновения модального окна перед кликом
            self.wait_for_element_to_disappear(OrderFeedLocators.ORDER_DETAILS_MODAL, time=5)
        except:
            pass
        self.find_clickable(OrderFeedLocators.ANY_ORDER_CARD, time=10)
        self.click_element(OrderFeedLocators.ANY_ORDER_CARD)

    def get_order_details_modal_title(self):
        return self.get_element_text(OrderFeedLocators.ORDER_DETAILS_MODAL_TITLE)

    def close_order_details_modal(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(OrderFeedLocators.ORDER_DETAILS_MODAL, time=5)
        except:
            pass
        self.find_clickable(OrderFeedLocators.ORDER_DETAILS_CLOSE_BUTTON, time=10)
        self.click_element(OrderFeedLocators.ORDER_DETAILS_CLOSE_BUTTON)
        self.wait_for_element_to_disappear(OrderFeedLocators.ORDER_DETAILS_MODAL, time=10)

    def get_total_orders_counter_value(self):
        return self.get_element_text(OrderFeedLocators.ORDERS_TOTAL_COUNTER)

    def get_today_orders_counter_value(self):
        return self.get_element_text(OrderFeedLocators.ORDERS_TODAY_COUNTER)

    def get_orders_in_progress_numbers(self):
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS_NUMBER, time=10)
        return [el.text for el in elements]

    def wait_for_feed_to_load(self):
        self.find_element(OrderFeedLocators.ORDER_FEED_TITLE, time=10)

    def wait_for_order_details_modal_to_be_visible(self):
        self.find_element(OrderFeedLocators.ORDER_DETAILS_MODAL_TITLE, time=10)

    def wait_for_total_counter_to_increase(self, initial_value, time=10):
        WebDriverWait(self.driver, time).until(
            lambda driver: int(self.get_element_text(OrderFeedLocators.ORDERS_TOTAL_COUNTER)) > int(initial_value)
        )

    def wait_for_today_counter_to_increase(self, initial_value, time=10):
        WebDriverWait(self.driver, time).until(
            lambda driver: int(self.get_element_text(OrderFeedLocators.ORDERS_TODAY_COUNTER)) > int(initial_value)
        )

    def wait_for_order_in_progress_section_to_contain_order(self, order_number, time=10):
        WebDriverWait(self.driver, time).until(
            lambda driver: order_number in self.get_orders_in_progress_numbers()
        )

    def is_order_feed_visible(self):
        try:
            return self.is_element_visible(OrderFeedLocators.ORDER_FEED_CONTAINER, time=10)
        except:
            return False

    def are_orders_displayed(self):
        try:
            orders = self.find_elements(OrderFeedLocators.ORDER_CARDS, time=10)
            return len(orders) > 0
        except:
            return False

    def is_order_statistics_visible(self):
        try:
            return self.is_element_visible(OrderFeedLocators.ORDER_STATISTICS, time=10)
        except:
            return False

    def get_first_order_number(self):
        return self.get_element_text(OrderFeedLocators.FIRST_ORDER_NUMBER)

    def get_modal_order_number(self):
        return self.get_element_text(OrderFeedLocators.MODAL_ORDER_NUMBER)

    def are_modal_ingredients_displayed(self):
        try:
            ingredients = self.find_elements(OrderFeedLocators.MODAL_INGREDIENTS, time=10)
            return len(ingredients) > 0
        except:
            return False

    def is_total_orders_counter_visible(self):
        try:
            return self.is_element_visible(OrderFeedLocators.ORDERS_TOTAL_COUNTER, time=10)
        except:
            return False

    def is_today_orders_counter_visible(self):
        try:
            return self.is_element_visible(OrderFeedLocators.ORDERS_TODAY_COUNTER, time=10)
        except:
            return False

    def is_in_progress_section_visible(self):
        try:
            return self.is_element_visible(OrderFeedLocators.IN_PROGRESS_SECTION, time=10)
        except:
            return False

    def get_in_progress_orders(self):
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS, time=10)
        return [el.text for el in elements]

    def are_user_orders_visible(self):
        try:
            return self.is_element_visible(OrderFeedLocators.USER_ORDERS_SECTION, time=10)
        except:
            return False

    def is_order_modal_visible(self):
        try:
            return self.is_element_visible(OrderFeedLocators.ORDER_DETAILS_MODAL, time=10)
        except:
            return False

    def create_new_order(self):
        """Создает новый заказ"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(OrderFeedLocators.ORDER_DETAILS_MODAL, time=5)
        except:
            pass
        self.find_clickable(OrderFeedLocators.CREATE_NEW_ORDER_BUTTON, time=10)
        self.click_element(OrderFeedLocators.CREATE_NEW_ORDER_BUTTON)

    def are_orders_displayed_in_history(self):
        """Проверяет, отображаются ли заказы в истории"""
        try:
            return self.is_element_visible(OrderFeedLocators.USER_ORDERS_SECTION, time=10)
        except:
            return False