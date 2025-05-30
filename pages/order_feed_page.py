from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.base_locators import BasePageLocators
from urls import Urls

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.FEED

    def go_to_site(self):
        return self.driver.get(self.url)

    def is_order_feed_title_visible(self):
        return self.is_element_present(OrderFeedLocators.ORDER_FEED_TITLE)

    def get_total_orders(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS)

    def get_today_orders(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS)

    def click_first_order(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER_IN_LIST)

    def is_order_modal_visible(self):
        return self.is_element_present(OrderFeedLocators.ORDER_MODAL)

    def close_order_modal(self):
        self.click_element(BasePageLocators.MODAL_CLOSE_BUTTON)

    def is_order_in_processing(self, order_id):
        return self.is_element_present(OrderFeedLocators.search_order_by_id(order_id))

    def get_order_number(self):
        return self.get_text(OrderFeedLocators.ORDER_NUMBER)

    def get_order_status(self):
        return self.get_text(OrderFeedLocators.ORDER_STATUS)

    def is_order_in_processing_list(self):
        return self.is_element_present(OrderFeedLocators.ORDER_IN_PROCESSING)
