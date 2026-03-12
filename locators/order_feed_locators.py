from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Элементы страницы
    ORDER_FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER_LIST = (By.XPATH, '//ul[contains(@class, "order-list")]')
    ORDER_ITEM = (By.XPATH, '//li[contains(@class, "order-item")]')

    # Детали заказа
    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "order-number")]')
    ORDER_STATUS = (By.XPATH, '//span[contains(@class, "order-status")]')

    # Счетчики
    TOTAL_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Модальные окна
    ORDER_MODAL = (By.XPATH, '//p[text() = "Cостав"]/ancestor::div[contains(@class, "container__Wo2l")]')
    MODAL_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    # Элементы списка заказов
    FIRST_ORDER_IN_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]/li[1]')
    ORDER_IN_PROCESSING = (By.XPATH, '//ul[contains(@class, "orderListReady")]/li[contains(@class, "default mb-2")]')

    @staticmethod
    def search_order_by_id(id_order):
        return (By.XPATH, f'.//ul[contains(@class, "OrderFeed_list")]//p[contains(text(), "{id_order}")]')

