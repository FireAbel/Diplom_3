import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.base_locators import BasePageLocators
from urls import Urls



class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы ленты заказов')
    def open_site(self):
        self.driver.get(Urls.FEED)
        self.wait_for_element_visibility(OrderFeedLocators.ORDER_FEED_TITLE)

    @allure.step('Клик по кнопке конструктора')
    def click_on_constructor_text(self):
        return self.click_element(BasePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка видимости заголовка ленты заказов')
    def is_order_feed_title_visible(self):
        return self.is_element_present(OrderFeedLocators.ORDER_FEED_TITLE)

    @allure.step('Получение счетчика "Выполнено за все время"')
    def get_total_orders(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS)

    @allure.step('Получение счетчика "Выполнено за сегодня"')
    def get_today_orders(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS)

    @allure.step('Клик по первому заказу в списке')
    def click_first_order(self):
        self.wait_for_element_visibility(OrderFeedLocators.FIRST_ORDER_IN_LIST)
        self.click_element(OrderFeedLocators.FIRST_ORDER_IN_LIST)
        self.wait_for_element_visibility(OrderFeedLocators.ORDER_MODAL)

    @allure.step('Проверка видимости модального окна заказа')
    def is_order_modal_visible(self):
        return self.is_element_present(OrderFeedLocators.ORDER_MODAL)

    @allure.step('Закрытие модального окна заказа')
    def close_order_modal(self):
        self.click_element(OrderFeedLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_invisibility(OrderFeedLocators.ORDER_MODAL)

    @allure.step('Проверка наличия заказа в работе')
    def is_order_in_processing(self, id_order):
        return self.is_element_present(OrderFeedLocators.search_order_by_id(id_order))

    @allure.step('Проверка наличия заказа в общей ленте заказов')
    def is_order_visible_in_feed(self, id_order):
        return self.is_element_present(OrderFeedLocators.search_order_by_id(id_order))
