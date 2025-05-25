from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    # Форма восстановления пароля
    RECOVERY_FORM = (By.CLASS_NAME, 'Auth_form__3qKeq')
    RESET_FORM = (By.CLASS_NAME, 'Auth_form__3qKeq')

    # Поля ввода
    EMAIL_INPUT = (By.XPATH, '//input[@type="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')

    # Кнопки
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    RESET_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    LOGIN_LINK = (By.XPATH, '//a[text()="Войти"]')

    # Иконки
    EYE_ICON = (By.CLASS_NAME, 'input__icon')

    # Сообщения
    ERROR_MESSAGE = (By.CLASS_NAME, 'input__error')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'Auth_success__3qKeq')

    # Модальные окна
    MODAL_OVERLAY = (By.CLASS_NAME, 'Modal_modal_overlay__x2ZCr')

    # Состояния пароля
    PASSWORD_VISIBLE = (By.XPATH, '//input[@type="text"]')
    PASSWORD_HIDDEN = (By.XPATH, '//input[@type="password"]')

    # Поля ввода
    SHOW_PASSWORD_ICON = (By.XPATH, '//div[contains(@class, "input__icon")]')

    # Иконка показа пароля
    SHOW_NEW_PASSWORD_ICON = (By.XPATH, '//input[@type="password" and @name="Введите новый пароль"]/following-sibling::div[contains(@class, "input__icon")]')
    # Форма смены пароля
    NEW_PASSWORD_FORM = (By.CLASS_NAME, 'Auth_form__3qKeq') 