import allure
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from urls import Urls
from data import UserTestData
from selenium.webdriver.support.ui import WebDriverWait

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка видимости заголовка восстановления пароля')
    def is_recovery_title_visible(self):
        return self.is_element_present(PasswordRecoveryLocators.RECOVERY_TITLE)

    @allure.step('Ввод email для восстановления')
    def input_email(self, email=UserTestData.TEST_USER_EMAIL):
        self.input_text(PasswordRecoveryLocators.EMAIL_INPUT, email)

    @allure.step('Клик по кнопке восстановления')
    def click_recovery_button(self):
        self.click_element(PasswordRecoveryLocators.RECOVERY_BUTTON)
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == Urls.RESET_PASSWORD)

    @allure.step('Клик по иконке показа пароля')
    def click_show_password(self):
        self.click_element(PasswordRecoveryLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка активности поля ввода пароля')
    def is_password_input_active(self):
        return self.is_element_present(PasswordRecoveryLocators.PASSWORD_INPUT_ACTIVE)

    @allure.step('Ввод нового пароля')
    def input_password(self, password=UserTestData.TEST_USER_PASSWORD):
        self.input_text(PasswordRecoveryLocators.PASSWORD_INPUT, password)

    @allure.step('Клик по кнопке сброса пароля')
    def click_reset_button(self):
        self.click_element(PasswordRecoveryLocators.RESET_BUTTON)
