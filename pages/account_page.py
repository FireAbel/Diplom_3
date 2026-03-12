import allure
from pages.base_page import BasePage
from locators.account_locators import AccountPageLocators
from urls import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.PROFILE

    @allure.step('Переход на страницу аккаунта')
    def go_to_site(self):
        self.driver.get(self.url)
        self.wait_for_page_load()

    @allure.step('Ожидание загрузки страницы')
    def wait_for_page_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(AccountPageLocators.PROFILE))

    @allure.step('Переход в профиль')
    def go_to_profile(self):
        self.wait_for_page_load()
        self.click_element(AccountPageLocators.PROFILE)

    @allure.step('Переход в историю заказов')
    def click_order_history(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY)

    @allure.step('Выход из аккаунта')
    def click_logout_button(self):
        self.click_element(AccountPageLocators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == Urls.LOGIN)