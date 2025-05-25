from selenium.webdriver.common.by import By

class OrderFeedLocators:

    # Основной контейнер
    ORDER_FEED_CONTAINER = (By.CLASS_NAME, 'OrderFeed_container')

    # Список заказов
    ORDER_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderList")]')
    ORDER_CARDS = (By.XPATH, '//li[contains(@class, "OrderFeed_order__")]')
    FIRST_ORDER = (By.XPATH, '(//li[contains(@class, "OrderFeed_order__")])[1]')
    FIRST_ORDER_NUMBER = (By.XPATH, '(//li[contains(@class, "OrderFeed_order__")])[1]//p[contains(@class, "OrderFeed_number")]')

    # Статистика заказов
    ORDER_STATISTICS = (By.CLASS_NAME, 'OrderFeed_statistics')

    # Модальное окно с деталями заказа
    ORDER_DETAILS_MODAL = (By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X')
    ORDER_DETAILS_POPUP = (By.XPATH, '//section[contains(@class, "Modal_modal_")]')
    MODAL_ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "Modal_number")]')
    MODAL_INGREDIENTS = (By.XPATH, '//ul[contains(@class, "Modal_ingredients")]//li')

    # Счетчики выполненных заказов
    DONE_ALL_TIME_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    DONE_TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Раздел "В работе"
    IN_PROGRESS_SECTION = (By.XPATH, '//div[contains(@class, "OrderFeed_boardStatus")]//h3[text()="В работе"]/following-sibling::ul')
    IN_PROGRESS_ORDERS = (By.XPATH, '//ul[contains(@class,"OrderFeed_ordersBoard")]/li[contains(@class, "text_color_inactive")]')

    # Секция заказов пользователя
    USER_ORDERS_SECTION = (By.CLASS_NAME, 'OrderHistory_orderHistory')

    ORDER_CARD = (By.XPATH, '//div[contains(@class,"OrderHistory_orderHistory")]//a')
    ORDER_MODAL = (By.CLASS_NAME, 'Modal_modal__contentBox__3gP0S')
    ORDER_MODAL_CLOSE = (By.XPATH, '//button[contains(@class,"Modal_modal__close__")]')

    ORDER_FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    ANY_ORDER_CARD = (By.CSS_SELECTOR, '.OrderFeed_item__wrapper')

    # Счетчики
    ORDERS_TOTAL_COUNTER = (By.CSS_SELECTOR, '.OrderFeed_digit__total')
    ORDERS_TODAY_COUNTER = (By.CSS_SELECTOR, '.OrderFeed_digit__today')

    # Секция "В работе"
    ORDERS_IN_PROGRESS_SECTION = (By.CSS_SELECTOR, '.OrderFeed_numbers__active')
    ORDERS_IN_PROGRESS_NUMBER = (By.CSS_SELECTOR, '.OrderFeed_numbers__active .OrderFeed_numbers__number')

    # Детали заказа (модальное окно)
    ORDER_DETAILS_MODAL_TITLE = (By.XPATH, '//h2[contains(text(), "Детали заказа")]')
    ORDER_DETAILS_CLOSE_BUTTON = (By.CSS_SELECTOR, '.Modal_modal__close')

    CREATE_NEW_ORDER_BUTTON = (By.XPATH, '//button[text()="Создать заказ"]')
