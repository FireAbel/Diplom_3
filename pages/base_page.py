import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.modal_overlay = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

    @allure.step('')
    def open(self, url):
        self.driver.get(url)

    @allure.step('')
    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('')
    def find_elements(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('')
    def find_clickable(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @allure.step('')
    def click_element(self, locator, time=3):
        # Ждем исчезновения модального окна перед кликом
        try:
            self.wait_for_element_to_disappear(self.modal_overlay)
        except:
            pass
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('')
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('')
    def get_element_text(self, locator, time=3):
        element = self.find_element(locator, time)
        return element.text

    @allure.step('')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('')
    def wait_for_element_visibility(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('')
    def wait_for_element_invisibility(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    @allure.step('')
    def drag_and_drop(self, source_locator, target_locator, time=3):
        source_element = self.find_element(source_locator, time)
        target_element = self.find_element(target_locator, time)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    @allure.step('')
    def send_keys(self, locator, text, time=3):
        # Ждем исчезновения модального окна перед вводом текста
        try:
            self.wait_for_element_to_disappear(self.modal_overlay)
        except:
            pass
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    @allure.step('')
    def is_element_visible(self, locator, time=3):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step('')
    def wait_for_element_clickable(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @allure.step('')
    def is_clickable(self, locator, time=3):
        try:
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
            return True
        except:
            return False

    @allure.step('')
    def wait_for_url_contains(self, url_part, time=3):
        WebDriverWait(self.driver, time).until(EC.url_contains(url_part))

    @allure.step('')
    def wait_for_element_to_disappear(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    @allure.step('')
    def is_element_focused(self, locator, time=3):
        element = self.find_element(locator, time)
        return element == self.driver.switch_to.active_element

    @allure.step('')
    def hover_over_element(self, locator, time=3):
        element = self.find_element(locator, time)
        ActionChains(self.driver).move_to_element(element).perform()