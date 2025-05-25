from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators as Locators
from data import Urls
import time

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.FORGOT_PASSWORD
        self.modal_overlay = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

    def open_page(self):
        """Открытие страницы восстановления пароля"""
        self.open(self.url)
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.wait_for_element_visibility(Locators.RECOVERY_FORM, time=10)

    def enter_email(self, email):
        """Ввод email в поле восстановления пароля"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        # Ждем, пока поле email станет кликабельным
        self.find_clickable(Locators.EMAIL_INPUT, time=10)
        self.send_keys(Locators.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Ввод нового пароля"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.send_keys(Locators.PASSWORD_INPUT, password)

    def click_recover_button(self):
        """Клик по кнопке 'Восстановить'"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        # Ждем, пока кнопка станет кликабельной
        self.find_clickable(Locators.RECOVER_BUTTON, time=10)
        self.click_element(Locators.RECOVER_BUTTON)
        # Ждем появления поля для ввода нового пароля
        self.wait_for_element_visibility(Locators.PASSWORD_INPUT, time=5)

    def click_login_link(self):
        """Клик по ссылке 'Войти'"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        # Ждем, пока ссылка станет кликабельной
        self.find_clickable(Locators.LOGIN_LINK, time=3)
        self.click_element(Locators.LOGIN_LINK)

    def click_show_password_icon(self):
        """Клик по иконке показать/скрыть пароль"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(Locators.MODAL_OVERLAY, time=5)
        except:
            pass
        # Ждем, пока иконка станет кликабельной
        self.find_clickable(Locators.EYE_ICON, time=10)
        self.click_element(Locators.EYE_ICON)

    def get_page_title(self):
        return self.get_text(Locators.PAGE_TITLE)

    def is_page_opened(self):
        return self.is_visible(Locators.PAGE_TITLE, time=3)

    def is_password_input_active(self):
        return False

    def is_password_input_focused(self):
        return False

    def is_page_title_visible(self):
        return self.is_visible(Locators.PAGE_TITLE, time=3)

    def click_password_visibility_toggle(self):
        pass

    def get_page_title_text(self):
        return self.get_element_text(Locators.RECOVERY_FORM)

    def wait_for_page_to_load(self):
        """Ожидает загрузки страницы"""
        self.wait_for_element_visibility(Locators.RECOVERY_FORM, time=3)

    def is_recovery_form_visible(self):
        """Проверяет видимость формы восстановления пароля"""
        try:
            return self.is_element_visible(Locators.RECOVERY_FORM, time=3)
        except:
            return False

    def is_success_message_visible(self):
        """Проверяет видимость сообщения об успешной отправке формы"""
        return self.is_element_visible(Locators.SUCCESS_MESSAGE, time=10)

    def wait_for_url_contains(self, url_part):
        """Ожидает, пока URL будет содержать указанную часть"""
        self.wait_for_url_to_contain(url_part, time=3)

    def is_password_field_active(self):
        """Проверка активности поля для ввода нового пароля"""
        try:
            return self.is_element_visible(Locators.PASSWORD_INPUT, time=10)
        except:
            return False

    def is_password_field_focused(self):
        """Проверка фокуса на поле пароля"""
        try:
            return self.is_element_focused(Locators.PASSWORD_FIELD, time=3)
        except:
            return False

    def is_error_message_visible(self):
        """Проверяет видимость сообщения об ошибке"""
        return self.is_element_visible(Locators.ERROR_MESSAGE, time=10)

    def wait_for_new_password_form(self, time=5):
        self.wait_for_element_visibility(Locators.NEW_PASSWORD_INPUT, time=time)

    def enter_new_password(self, password):
        self.send_keys(Locators.NEW_PASSWORD_INPUT, password)

    def click_show_new_password_icon(self):
        self.click_element(Locators.SHOW_NEW_PASSWORD_ICON)

    def is_new_password_input_visible(self):
        return self.is_element_visible(Locators.NEW_PASSWORD_INPUT)

    def is_login_form_visible(self):
        """Проверяет видимость формы логина после перехода"""
        from locators.login_page_locators import LoginPageLocators
        try:
            return self.is_element_visible(LoginPageLocators.LOGIN_FORM, time=3)
        except:
            return False

    def is_password_visible(self):
        try:
            return self.is_element_visible(Locators.PASSWORD_VISIBLE, time=10)
        except:
            return False

    def is_password_hidden(self):
        try:
            return self.is_element_visible(Locators.PASSWORD_HIDDEN, time=10)
        except:
            return False

    def get_error_message_text(self):
        return self.get_element_text(Locators.ERROR_MESSAGE)

    def get_success_message_text(self):
        return self.get_element_text(Locators.SUCCESS_MESSAGE)

    def is_reset_form_visible(self):
        try:
            return self.is_element_visible(Locators.RESET_FORM, time=10)
        except:
            return False

    def is_reset_button_visible(self):
        try:
            return self.is_element_visible(Locators.RESET_BUTTON, time=10)
        except:
            return False

    def is_reset_button_enabled(self):
        try:
            return self.is_element_enabled(Locators.RESET_BUTTON, time=10)
        except:
            return False

    def is_reset_button_disabled(self):
        try:
            return not self.is_element_enabled(Locators.RESET_BUTTON, time=10)
        except:
            return False

    def is_reset_button_clickable(self):
        try:
            return self.is_element_clickable(Locators.RESET_BUTTON, time=10)
        except:
            return False

    def is_reset_button_not_clickable(self):
        try:
            return not self.is_element_clickable(Locators.RESET_BUTTON, time=10)
        except:
            return False

    def is_reset_button_highlighted(self):
        try:
            return self.is_element_highlighted(Locators.RESET_BUTTON, time=10)
        except:
            return False

    def is_reset_button_not_highlighted(self):
        try:
            return not self.is_element_highlighted(Locators.RESET_BUTTON, time=10)
        except:
            return False
