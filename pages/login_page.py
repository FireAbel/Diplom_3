import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from locators.base_locators import BasePageLocators
from data import UserTestData
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы входа')
    def open_site(self):
        self.driver.get(Urls.LOGIN)
        self.wait_for_element_visibility(LoginLocators.LOGIN_BUTTON)

    @allure.step('Клик по ссылке восстановления пароля')
    def click_forgot_password(self):
        self.click_element(LoginLocators.RECOVERY_LINK)

    @allure.step('Вход в систему')
    def login(self, email=UserTestData.TEST_USER_EMAIL, password=UserTestData.TEST_USER_PASSWORD):
        self.input_email(email)
        self.input_password(password)
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
        self.click_element(LoginLocators.LOGIN_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(Urls.BASE_URL))

    @allure.step('Ввод email')
    def input_email(self, email=UserTestData.TEST_USER_EMAIL):
        self.input_text(LoginLocators.EMAIL_INPUT, email)

    @allure.step('Ввод пароля')
    def input_password(self, password=UserTestData.TEST_USER_PASSWORD):
        self.input_text(LoginLocators.PASSWORD_INPUT, password)

