from pages import base_page
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from data import UserTestData
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_site(self):
        self.driver.get(Urls.LOGIN)

    def click_forgot_password(self):
        self.click_element(LoginLocators.RECOVERY_LINK)



    def login(self, email=UserTestData.TEST_USER_EMAIL, password=UserTestData.TEST_USER_PASSWORD):
        self.input_email(email)
        self.input_password(password)
        try:
            # Ждем, пока кнопка станет кликабельной
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
            )
            # Прокручиваем к кнопке
            self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
            # Небольшая пауза для стабильности
            time.sleep(1)
            # Кликаем по кнопке
            login_button.click()
        except TimeoutException:
            print("Кнопка входа не найдена или не кликабельна")
            raise

    def input_email(self, email=UserTestData.TEST_USER_EMAIL):
        self.input_text(LoginLocators.EMAIL_INPUT, email)

    def input_password(self, password=UserTestData.TEST_USER_PASSWORD):
        self.input_text(LoginLocators.PASSWORD_INPUT, password)

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

    def go_to_recovery(self):
        self.click_element(LoginLocators.RECOVERY_LINK)

    def is_login_button_visible(self):
        return self.is_element_present(LoginLocators.LOGIN_BUTTON)
