from pages.base_page import BasePage
from locators.account_locators import AccountPageLocators
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_site(self):
        self.driver.get(self.url)
        self.wait_for_page_load()

    def wait_for_page_load(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(AccountPageLocators.PROFILE_TAB)
            )
        except TimeoutException:
            pass

    def go_to_profile(self):
        self.wait_for_page_load()
        self.click_element(AccountPageLocators.PROFILE_TAB)

    def click_order_history(self):
        self.wait_for_page_load()
        self.click_element(AccountPageLocators.ORDER_HISTORY_TAB)

    def click_logout_button(self):
        self.wait_for_page_load()
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)

    def wait_for_modal_to_disappear(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(("xpath", "//div[contains(@class, 'Modal_modal_overlay')]"))
            )
        except TimeoutException:
            pass  # Если модальное окно не появилось, продолжаем выполнение

    def click_element(self, locator, timeout=10):
        self.wait_for_modal_to_disappear(timeout)
        super().click_element(locator)

    def save_changes(self):
        self.click_element(AccountPageLocators.SAVE_BUTTON)

    def get_last_order_id(self):
        return self.get_text(AccountPageLocators.LAST_ORDER_IN_HISTORY)

    def is_profile_tab_visible(self):
        return self.is_element_present(AccountPageLocators.PROFILE_TAB)

    def is_order_history_tab_visible(self):
        return self.is_element_present(AccountPageLocators.ORDER_HISTORY_TAB)
