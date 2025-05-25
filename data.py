class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    LOGIN = f'{BASE_URL}login'
    REGISTER = f'{BASE_URL}register'
    FORGOT_PASSWORD = f'{BASE_URL}forgot-password'
    PROFILE = f'{BASE_URL}account/profile'
    RESET_PASSWORD = f'{BASE_URL}reset-password'
    ORDER_HISTORY = f'{BASE_URL}account/order-history'
    FEED = f'{BASE_URL}feed'
    ORDER_FEED = FEED  # Алиас для обратной совместимости

class UserTestData:
    TEST_USER_EMAIL = 'alekseevnikita15.001@yandex.ru'
    TEST_USER_PASSWORD = 'htedcxa'