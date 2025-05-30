from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from locators.base_locators import BasePageLocators
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_site(self):
        self.driver.get(Urls.BASE_URL)

    def create_order(self):
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    def get_bun_counter(self):
        return self.get_text(MainPageLocators.BUN_COUNTER)

    def get_sauce_counter(self):
        return self.get_text(MainPageLocators.SAUCE_COUNTER)

    def get_filling_counter(self):
        return self.get_text(MainPageLocators.FILLING_COUNTER)

    def click_bun_card(self):
        self.click_element(MainPageLocators.BUN_CARD)

    def click_sauce_card(self):
        self.click_element(MainPageLocators.SAUCE_CARD)

    def click_filling_card(self):
        self.click_element(MainPageLocators.FILLING_CARD)

    def click_buns_tab(self):
        self.click_element(MainPageLocators.BUNS_TAB)

    def click_sauces_tab(self):
        self.click_element(MainPageLocators.SAUCES_TAB)

    def click_fillings_tab(self):
        self.click_element(MainPageLocators.FILLINGS_TAB)

    def is_ingredient_details_visible(self):
        return self.is_element_present(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    def close_ingredient_details(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def get_order_id(self):
        return self.get_text(MainPageLocators.ORDER_ID)

    def is_order_status_visible(self):
        return self.is_element_present(MainPageLocators.ORDER_STATUS)

    def drag_ingredient_to_constructor(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        constructor = self.find_element(MainPageLocators.CONSTRUCTOR_BURGER)
        self.driver.execute_script("arguments[0].dragAndDrop(arguments[1])", ingredient, constructor)

    def click_account_button(self):
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    def click_order_feed_button(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)

    def click_login_button(self):
        self.wait_for_element_visible(MainPageLocators.LOGIN_BUTTON)
        self.click_element(MainPageLocators.LOGIN_BUTTON)

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
