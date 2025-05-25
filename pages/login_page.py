from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as Locators
from data import Urls

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.LOGIN
        self.modal_overlay = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

    def open_page(self):
        self.driver.get(Urls.LOGIN)
        self.wait_for_element_visibility(Locators.EMAIL_INPUT, time=3)
        self.wait_for_element_visibility(Locators.PASSWORD_INPUT, time=3)

    def enter_email(self, email):
        self.send_keys(Locators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(Locators.PASSWORD_INPUT, password)

    def click_login_button(self):
        # Ждем исчезновения модального окна перед кликом
        try:
            self.wait_for_element_to_disappear(self.modal_overlay, time=3)
        except:
            pass
        self.click_element(Locators.LOGIN_BUTTON)

    def login_user(self, email, password):
        """Выполняет вход пользователя"""
        # Ждем загрузки страницы
        self.wait_for_element_visibility(Locators.LOGIN_FORM, time=3)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def get_login_title_text(self):
        return self.get_element_text(Locators.LOGIN_LINK)

    def click_register_link(self):
        # Ждем исчезновения модального окна перед кликом
        try:
            self.wait_for_element_to_disappear(self.modal_overlay, time=3)
        except:
            pass
        self.click_element(Locators.REGISTER_LINK)

    def click_forgot_password_link(self):
        """Нажимает ссылку 'Забыли пароль'"""
        # Ждем исчезновения модального окна перед кликом
        try:
            self.wait_for_element_to_disappear(self.modal_overlay, time=3)
        except:
            pass
        self.click_element(Locators.FORGOT_PASSWORD_LINK)

    def wait_for_login_title_to_be_visible(self):
        self.find_element(Locators.LOGIN_LINK, time=3)

    def is_login_form_visible(self):
        return self.is_element_visible(Locators.EMAIL_INPUT, time=3) and self.is_element_visible(Locators.PASSWORD_INPUT, time=3)

    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url