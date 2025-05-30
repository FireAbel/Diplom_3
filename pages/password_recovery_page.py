from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from urls import Urls
from data import UserTestData

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_recovery_title_visible(self):
        return self.is_element_present(PasswordRecoveryLocators.RECOVERY_TITLE)

    def input_email(self, email=UserTestData.TEST_USER_EMAIL):
        self.input_text(PasswordRecoveryLocators.EMAIL_INPUT, email)

    def click_recovery_button(self):
        self.click_element(PasswordRecoveryLocators.RECOVERY_BUTTON)

    def click_show_password(self):
        self.click_element(PasswordRecoveryLocators.SHOW_PASSWORD_ICON)

    def is_password_input_active(self):
        return self.is_element_present(PasswordRecoveryLocators.PASSWORD_INPUT_ACTIVE)

    def input_password(self, password=UserTestData.TEST_USER_PASSWORD):
        self.input_text(PasswordRecoveryLocators.PASSWORD_INPUT, password)

    def click_reset_button(self):
        self.click_element(PasswordRecoveryLocators.RESET_BUTTON)
