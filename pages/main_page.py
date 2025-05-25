from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from data import Urls, UserTestData
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.BASE_URL

    def open_page(self):
        self.open(self.url)
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass

    def click_constructor_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.CONSTRUCTOR_BUTTON, time=10)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.ORDER_FEED_BUTTON, time=10)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_login_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.LOGIN_BUTTON, time=10)
        self.click_element(MainPageLocators.LOGIN_BUTTON)

    def click_personal_account_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON, time=10)
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_ingredient(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.INGREDIENT_ITEM, time=10)
        self.click_element(MainPageLocators.INGREDIENT_ITEM)

    def close_modal(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.MODAL_CLOSE_BUTTON, time=10)
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def click_buns_tab(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.BUNS_TAB, time=10)
        self.click_element(MainPageLocators.BUNS_TAB)

    def click_sauces_tab(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.SAUCES_TAB, time=10)
        self.click_element(MainPageLocators.SAUCES_TAB)

    def click_fillings_tab(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.FILLINGS_TAB, time=10)
        self.click_element(MainPageLocators.FILLINGS_TAB)

    def click_ingredient_card(self, ingredient_locator):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(ingredient_locator, time=10)
        self.click_element(ingredient_locator)

    def get_ingredient_details_modal_title(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

    def close_ingredient_details_modal(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON, time=10)
        self.click_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    def get_ingredient_counter_value(self, ingredient_locator):
        ingredient_card = self.find_element(ingredient_locator, time=10)
        counter_element = ingredient_card.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return counter_element.text

    def drag_ingredient_to_constructor(self, ingredient_locator):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.drag_and_drop(ingredient_locator, MainPageLocators.BURGER_CONSTRUCTOR_AREA)

    def click_place_order_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.PLACE_ORDER_BUTTON, time=10)
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_order_number_from_modal(self):
        self.find_element(MainPageLocators.ORDER_NUMBER_MODAL_TITLE, time=10)
        return self.get_element_text(MainPageLocators.ORDER_NUMBER_TEXT)

    def wait_for_ingredient_details_modal_to_be_visible(self):
        self.find_element(MainPageLocators.INGREDIENT_DETAILS_MODAL_TITLE, time=10)

    def wait_for_order_modal_to_be_visible(self):
        self.find_element(MainPageLocators.ORDER_NUMBER_MODAL_TITLE, time=10)

    def is_order_button_visible(self):
        try:
            self.find_element(MainPageLocators.PLACE_ORDER_BUTTON, time=10)
            return True
        except:
            return False

    def click_personal_account_header_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(BasePageLocators.PERSONAL_ACCOUNT_BUTTON, time=10)
        self.click_element(BasePageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_order_feed_header_link(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(BasePageLocators.ORDER_FEED_LINK, time=10)
        self.click_element(BasePageLocators.ORDER_FEED_LINK)

    def click_constructor_header_link(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(BasePageLocators.CONSTRUCTOR_LINK, time=10)
        self.click_element(BasePageLocators.CONSTRUCTOR_LINK)

    def click_stellar_burgers_logo(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(BasePageLocators.STELLAR_BURGERS_LOGO, time=10)
        self.click_element(BasePageLocators.STELLAR_BURGERS_LOGO)

    def add_ingredients_to_order(self):
        """Добавляет стандартный набор ингредиентов для создания заказа"""
        self.click_buns_tab()
        self.drag_ingredient_to_constructor(MainPageLocators.FIRST_BUN)
        
        self.click_fillings_tab()
        self.drag_ingredient_to_constructor(MainPageLocators.FIRST_FILLING)
        
        self.click_sauces_tab()
        self.drag_ingredient_to_constructor(MainPageLocators.FIRST_SAUCE)

    def click_order_button(self):
        """Нажимает кнопку 'Оформить заказ'"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.PLACE_ORDER_BUTTON, time=10)
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_order_number(self):
        """Получает номер заказа из модального окна"""
        return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    def wait_for_order_success(self):
        """Ожидает успешного оформления заказа"""
        self.wait_for_element(MainPageLocators.ORDER_SUCCESS_MESSAGE, time=10)

    def is_buns_tab_active(self):
        """Проверяет, активна ли вкладка 'Булки'"""
        return self.is_element_visible(MainPageLocators.BUNS_TAB_ACTIVE, time=10)

    def is_sauces_tab_active(self):
        """Проверяет, активна ли вкладка 'Соусы'"""
        return self.is_element_visible(MainPageLocators.SAUCES_TAB_ACTIVE, time=10)

    def is_fillings_tab_active(self):
        """Проверяет, активна ли вкладка 'Начинки'"""
        return self.is_element_visible(MainPageLocators.FILLINGS_TAB_ACTIVE, time=10)

    def is_buns_section_visible(self):
        """Проверяет видимость секции с булками"""
        return self.is_element_visible(MainPageLocators.BUNS_SECTION, time=10)

    def is_sauces_section_visible(self):
        """Проверяет видимость секции с соусами"""
        return self.is_element_visible(MainPageLocators.SAUCES_SECTION, time=10)

    def is_fillings_section_visible(self):
        """Проверяет видимость секции с начинками"""
        return self.is_element_visible(MainPageLocators.FILLINGS_SECTION, time=10)

    def drag_bun_to_constructor(self):
        """Перетаскивает булку в конструктор"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.drag_and_drop(MainPageLocators.FIRST_BUN, MainPageLocators.BURGER_CONSTRUCTOR_AREA)

    def drag_sauce_to_constructor(self):
        """Перетаскивает соус в конструктор"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.drag_and_drop(MainPageLocators.FIRST_SAUCE, MainPageLocators.BURGER_CONSTRUCTOR_AREA)

    def drag_filling_to_constructor(self):
        """Перетаскивает начинку в конструктор"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.drag_and_drop(MainPageLocators.FIRST_FILLING, MainPageLocators.BURGER_CONSTRUCTOR_AREA)

    def is_bun_in_constructor(self):
        """Проверяет наличие булки в конструкторе"""
        return self.is_element_visible(MainPageLocators.TOP_BUN_IN_CONSTRUCTOR, time=10) and \
               self.is_element_visible(MainPageLocators.BOTTOM_BUN_IN_CONSTRUCTOR, time=10)

    def is_sauce_in_constructor(self):
        """Проверяет наличие соуса в конструкторе"""
        return self.is_element_visible(MainPageLocators.FILLING_IN_CONSTRUCTOR, time=10)

    def is_filling_in_constructor(self):
        """Проверяет наличие начинки в конструкторе"""
        return self.is_element_visible(MainPageLocators.FILLING_IN_CONSTRUCTOR, time=10)

    def click_first_ingredient(self):
        """Кликает по первому ингредиенту в списке"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.FIRST_INGREDIENT, time=10)
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    def is_ingredient_modal_visible(self):
        """Проверяет видимость модального окна с деталями ингредиента"""
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL, time=10)

    def is_ingredient_details_visible(self):
        """Проверяет видимость деталей ингредиента в модальном окне"""
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_CONTENT, time=10)

    def login_user(self, email=None, password=None):
        """Выполняет вход пользователя"""
        if email is None:
            email = UserTestData.TEST_USER_EMAIL
        if password is None:
            password = UserTestData.TEST_USER_PASSWORD
            
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login_button()

    def get_ingredient_count(self):
        """Получает значение счетчика ингредиентов"""
        return self.get_ingredient_counter_value(MainPageLocators.FIRST_INGREDIENT)

    def add_ingredient_to_order(self):
        """Добавляет ингредиент в заказ"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.drag_ingredient_to_constructor(MainPageLocators.FIRST_INGREDIENT)

    def submit_order(self):
        """Оформляет заказ"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.click_place_order_button()
        self.wait_for_order_success()

    def click_submit_order_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.SUBMIT_ORDER_BUTTON, time=10)
        self.click_element(MainPageLocators.SUBMIT_ORDER_BUTTON)

    def click_close_modal_button(self):
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.CLOSE_MODAL_BUTTON, time=10)
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    def is_ingredient_details_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL, time=10)

    def is_order_modal_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL, time=10)

    def is_order_number_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_NUMBER, time=10)

    def get_order_number(self):
        return self.get_element_text(MainPageLocators.ORDER_NUMBER)

    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR, time=10)

    def is_order_feed_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_FEED, time=10)

    def is_ingredient_modal_title_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_TITLE, time=10)

    def is_ingredient_modal_image_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_IMAGE, time=10)

    def is_ingredient_modal_description_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_DESCRIPTION, time=10)

    def is_ingredient_modal_nutrition_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_NUTRITION, time=10)

    def is_ingredient_modal_close_button_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON, time=10)

    def is_order_modal_title_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_TITLE, time=10)

    def is_order_modal_number_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_NUMBER, time=10)

    def is_order_modal_status_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_STATUS, time=10)

    def is_order_modal_ingredients_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_INGREDIENTS, time=10)

    def is_order_modal_total_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_TOTAL, time=10)

    def is_order_modal_close_button_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON, time=10)

    def wait_for_ingredient_details_modal_to_disappear(self):
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_DETAILS_MODAL, time=10)

    def wait_for_order_modal_to_disappear(self):
        self.wait_for_element_to_disappear(MainPageLocators.ORDER_MODAL, time=10)

    def wait_for_order_number_to_be_visible(self):
        self.find_element(MainPageLocators.ORDER_NUMBER, time=10)

    def is_order_submitted(self):
        """Проверяет, отправлен ли заказ"""
        try:
            return self.is_element_visible(MainPageLocators.ORDER_MODAL, time=10)
        except:
            return False

    def close_ingredient_modal(self):
        """Закрывает модальное окно с деталями ингредиента"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON, time=10)
        self.click_element(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL, time=10)

    def close_order_modal(self):
        """Закрывает модальное окно с деталями заказа"""
        try:
            # Ждем исчезновения модального окна, если оно есть
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY, time=5)
        except:
            pass
        self.find_clickable(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON, time=10)
        self.click_element(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)
        self.wait_for_element_to_disappear(MainPageLocators.ORDER_MODAL, time=10)