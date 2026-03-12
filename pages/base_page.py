import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
from locators.base_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие главной страницы')
    def open_site(self):
        return self.driver.get(Urls.BASE_URL)

    @allure.step('Получение текущего url')
    def get_current_site(self):
        return self.driver.current_url

    @allure.step('Поиск элемента на странице')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод текста в поле')
    def input_text(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание скрытия элемента')
    def wait_for_element_invisibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    @allure.step('Проверка наличия элемента на странице')
    def is_element_present(self, locator, time=10):
        try:
            self.find_element(locator, time)
            return True
        except:
            return False

    @allure.step('Ожидание кликабельности кнопки')
    def wait_for_button_active(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидание закрытия элемента')
    def wait_close_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Проверка невидимости элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    @allure.step('Ожидание изменения элемента')
    def wait_text_element_to_change(self, test_locator, value):
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(test_locator, value))