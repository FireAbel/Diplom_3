from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators as Locators
from data import Urls

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.PROFILE

    def open_page(self):
        self.open(self.url)
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.wait_for_element_visibility(Locators.PROFILE_CONTENT, time=10)

    def click_account_button(self):
        """Нажимает кнопку личного кабинета"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(Locators.ACCOUNT_BUTTON, time=10)
        self.click_element(Locators.ACCOUNT_BUTTON)

    def is_profile_visible(self):
        """Проверяет видимость профиля"""
        try:
            return self.is_element_visible(Locators.PROFILE_CONTENT, time=10)
        except:
            return False

    def click_profile_tab(self):
        """Нажимает вкладку 'Профиль'"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(Locators.PROFILE_TAB, time=10)
        self.click_element(Locators.PROFILE_TAB)

    def click_order_history_tab(self):
        """Нажимает вкладку 'История заказов'"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(Locators.ORDER_HISTORY_TAB, time=10)
        self.click_element(Locators.ORDER_HISTORY_TAB)

    def is_profile_tab_active(self):
        """Проверяет, активна ли вкладка 'Профиль'"""
        try:
            return self.is_element_visible(Locators.PROFILE_TAB_ACTIVE, time=10)
        except:
            return False

    def is_order_history_tab_active(self):
        """Проверяет, активна ли вкладка 'История заказов'"""
        try:
            return self.is_element_visible(Locators.ORDER_HISTORY_TAB_ACTIVE, time=10)
        except:
            return False

    def is_profile_content_visible(self):
        """Проверяет видимость содержимого профиля"""
        try:
            return self.is_element_visible(Locators.PROFILE_CONTENT, time=10)
        except:
            return False

    def is_order_history_visible(self):
        """Проверяет видимость истории заказов"""
        try:
            return self.is_element_visible(Locators.ORDER_HISTORY_CONTENT, time=10)
        except:
            return False

    def click_logout_button(self):
        """Нажимает кнопку выхода"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(Locators.LOGOUT_BUTTON, time=10)
        self.click_element(Locators.LOGOUT_BUTTON)

    def get_profile_menu_text(self):
        return self.get_element_text(Locators.PROFILE_MENU_LINK)

    def click_order_history_link(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(Locators.ORDER_HISTORY_LINK, time=10)
        self.click_element(Locators.ORDER_HISTORY_LINK)

    def is_order_history_card_visible(self):
        try:
            return self.is_element_visible(Locators.ORDER_HISTORY_ORDER_CARD, time=10)
        except:
            return False

    def wait_for_profile_menu_link_to_be_visible(self):
        self.find_element(Locators.PROFILE_MENU_LINK, time=5)

    def click_profile_link(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(Locators.PROFILE_LINK, time=10)
        self.click_element(Locators.PROFILE_LINK)

    def is_logout_button_visible(self):
        try:
            return self.is_element_visible(Locators.LOGOUT_BUTTON, time=10)
        except:
            return False

    def is_order_history_link_visible(self):
        try:
            return self.is_element_visible(Locators.ORDER_HISTORY_LINK, time=10)
        except:
            return False

    def is_order_history_menu_link_visible(self):
        try:
            return self.is_element_visible(Locators.ORDER_HISTORY_MENU_LINK, time=10)
        except:
            return False

    def is_profile_link_visible(self):
        try:
            return self.is_element_visible(Locators.PROFILE_LINK, time=10)
        except:
            return False