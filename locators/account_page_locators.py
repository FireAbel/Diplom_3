from selenium.webdriver.common.by import By

class AccountPageLocators:

    # Элементы бокового меню личного кабинета
    PROFILE_MENU_LINK = (By.XPATH, "//a[contains(@href, '/profile')]")
    ORDER_HISTORY_MENU_LINK = (By.XPATH, "//a[contains(@href, '/profile/orders')]")

    # Элементы на странице "История заказов" (если они специфичны для этой вкладки ЛК)
    ORDER_HISTORY_ORDER_CARD = (By.CLASS_NAME, 'order-card')

    # Кнопки навигации
    ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'account-button')]")
    PROFILE_TAB_ACTIVE = (By.XPATH, "//button[contains(@class, 'active') and contains(text(), 'Профиль')]")
    ORDER_HISTORY_TAB_ACTIVE = (By.XPATH, "//button[contains(@class, 'active') and contains(text(), 'История заказов')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, '/profile')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href, '/profile/orders')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    PROFILE_CONTENT = (By.CLASS_NAME, 'profile-content')
    
    # Модальное окно
    MODAL_OVERLAY = (By.CLASS_NAME, 'Modal_modal_overlay__x2ZCr')

    # История заказов
    ORDER_HISTORY_TAB = (By.XPATH, "//button[contains(text(), 'История заказов')]")
    ORDER_HISTORY_CONTENT = (By.CLASS_NAME, 'order-history-content')
