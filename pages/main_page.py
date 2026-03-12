import allure
from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from locators.base_locators import BasePageLocators
from urls import Urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие главной страницы')
    def open_site(self):
        self.driver.get(Urls.BASE_URL)

    @allure.step('Создание заказа')
    def create_order(self):
        self.wait_for_element_invisibility(BasePageLocators.MODAL_WINDOW)
        self.wait_for_button_active(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получение счетчика булок')
    def get_bun_counter(self):
        return self.get_text(MainPageLocators.BUN_COUNTER)

    @allure.step('Получение счетчика соусов')
    def get_sauce_counter(self):
        return self.get_text(MainPageLocators.SAUCE_COUNTER)

    @allure.step('Получение счетчика начинок')
    def get_filling_counter(self):
        return self.get_text(MainPageLocators.FILLING_COUNTER)

    #Я понимаю, что JS это не самое лучшее решение для автоматизации на питоне, но через ActionChains у меня совсем не хотело запускаться от слова совсем
    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient(self, ingredient_locator, constructor_locator):
        ingredient = self.find_element(ingredient_locator)
        constructor = self.find_element(constructor_locator)
        self.driver.execute_script("""
            function simulateDragAndDrop(sourceNode, destinationNode) {
                var EVENT_TYPES = {
                    DRAG_END: 'dragend',
                    DRAG_START: 'dragstart',
                    DROP: 'drop'
                }

                function createEvent(type) {
                    var event = new Event(type, { bubbles: true, cancelable: true });
                    Object.defineProperty(event, 'dataTransfer', {
                        get: function() {
                            return {
                                data: {},
                                setData: function(type, val) {
                                    this.data[type] = val;
                                },
                                getData: function(type) {
                                    return this.data[type];
                                }
                            };
                        }
                    });
                    return event;
                }

                function dispatchEvent(node, type, event) {
                    node.dispatchEvent(event);
                }

                var dragstartEvent = createEvent(EVENT_TYPES.DRAG_START);
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragstartEvent);

                var dropEvent = createEvent(EVENT_TYPES.DROP);
                dropEvent.dataTransfer = dragstartEvent.dataTransfer;
                dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent);

                var dragendEvent = createEvent(EVENT_TYPES.DRAG_END);
                dragendEvent.dataTransfer = dragstartEvent.dataTransfer;
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragendEvent);
            }
            simulateDragAndDrop(arguments[0], arguments[1]);
        """, ingredient, constructor)

    @allure.step('Ожидание номера заказа')
    def wait_for_order_number_visibility(self):
        self.wait_for_element_visibility(MainPageLocators.ID_ORDER)

    @allure.step('Получение номера заказа')
    def get_order_id(self):
        self.wait_text_element_to_change(MainPageLocators.ID_ORDER, '9999')
        id_order = self.get_text(MainPageLocators.ID_ORDER)
        return f"0{id_order}"

    @allure.step('Закрытие модального окна заказа')
    def close_modal_order(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_ORDER)

    @allure.step('Проверка видимости идентификатора заказа')
    def is_order_identified_visible(self):
        return self.is_element_present(MainPageLocators.ORDER_IDENTIFICATE)

    @allure.step('Клик по кнопке "Личный кабинет" в шапке')
    def click_account_button(self):
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Клик по ссылке "Лента заказов"')
    def click_order_feed_button(self):
        self.click_element(BasePageLocators.ORDER_FEED_LINK)

    @allure.step('Клик по ингредиенту')
    def click_bun_card(self):
        self.wait_for_element_visibility(MainPageLocators.BUN_CARD)
        self.click_element(MainPageLocators.BUN_CARD)

    @allure.step('Проверка видимости модального окна')
    def check_visible_bun_card(self):
        self.wait_for_element_visibility(MainPageLocators.INGREDIENT_MODAL_TITLE)
        return self.wait_for_element_visibility(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Проверка невидимости модального окна')
    def check_invisible_bun_card(self):
        self.wait_close_element(MainPageLocators.INGREDIENT_MODAL_TITLE)
        return self.check_invisibility(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Закрытие модального окна булки')
    def close_bun_card(self):
        self.wait_for_element_visibility(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

