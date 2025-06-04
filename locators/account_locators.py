from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Вкладки навигации
    PROFILE = (By.XPATH, '//a[text()="Профиль"]')
    ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]')

    # Кнопки
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выход")]')


    # Элементы истории заказов
    LAST_ORDER_IN_HISTORY = (By.XPATH, ".//ul[contains(@class, 'OrderHistory')]/li[last()]//"
                                       "div[contains(@class, 'Box__3lgbs mb-6')]/p[contains(@class, 'digits-default')]")
