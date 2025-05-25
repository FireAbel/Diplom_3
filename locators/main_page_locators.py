from selenium.webdriver.common.by import By

class MainPageLocators:

    # Модальное окно
    MODAL_OVERLAY = (By.CLASS_NAME, 'Modal_modal_overlay__x2ZCr')

    # Кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[text()="Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//a[text()="Лента Заказов"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[contains(@href, "/account")]')
    LOGO_BUTTON = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo")]')

    # Разделы конструктора
    BUNS_TAB = (By.XPATH, '//span[text()="Булки"]')
    SAUCES_TAB = (By.XPATH, '//span[text()="Соусы"]')
    FILLINGS_TAB = (By.XPATH, '//span[text()="Начинки"]')

    # Ингредиенты
    INGREDIENT_ITEM = (By.CLASS_NAME, 'BurgerIngredient_ingredient__1TVf6')
    FIRST_INGREDIENT = (By.XPATH, '(//ul[@class="BurgerIngredients_ingredients__list__2A-mT"]//li)[1]')
    INGREDIENT_COUNTER = (By.CLASS_NAME, 'Counter_counter__num__3nue1')

    # Модальные окна
    INGREDIENT_MODAL = (By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X')
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, 'Modal_modal__close__TnseK')
    ORDER_SUCCESS_MODAL = (By.XPATH, '//div[contains(@class, "modal_opened")]//h2[text()="Идентификатор заказа"]')
    ORDER_NUMBER = (
    By.XPATH, '//div[contains(@class, "modal_opened")]//h2[text()="Идентификатор заказа"]/following-sibling::p')

    # Область конструктора
    CONSTRUCTOR_AREA = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Лента заказов
    ORDER_FEED_TAB = (By.XPATH, '//p[text()="Лента Заказов"]')
    ORDER_ITEM = (By.CLASS_NAME, 'OrderFeed_orderFeed__item__1T3T2')
    TOTAL_ORDERS_COUNTER = (By.CLASS_NAME, 'OrderFeed_orderFeed__total__1T3T2')

    # История заказов
    ORDER_HISTORY_TAB = (By.XPATH, '//a[contains(@href, "/account/orders")]')

    # Локаторы конкретных ингредиентов (примерные, завязаны на текст)
    BUN_EXAMPLE = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::a')
    SAUCE_EXAMPLE = (By.XPATH, '//p[text()="Соус Spicy-X"]/ancestor::a')
    FILLING_EXAMPLE = (By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]/ancestor::a')

    ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')

    BUN_INGREDIENT = (By.XPATH, '//span[text()="Флюоресцентная булка R2-D3"]')
    SAUCE_INGREDIENT = (By.XPATH, '//span[text()="Соус Spicy-X"]')
    MAIN_INGREDIENT = (By.XPATH, '//span[text()="Мясо бессмертных моллюсков Protostomia"]')

    MODAL_WINDOW = (By.CLASS_NAME, 'Modal_modal__contentBox__3gP0S')

    # Элементы ингредиентов
    ANY_INGREDIENT_CARD = (By.CSS_SELECTOR, '.BurgerIngredients_ingredients__item')
    BUN_CARD = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::div[contains(@class, "BurgerIngredients_ingredients__item")]')
    SAUCE_CARD = (By.XPATH, '//p[text()="Соус Spicy-X"]/ancestor::div[contains(@class, "BurgerIngredients_ingredients__item")]')
    FILLING_CARD = (By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protoceratops"]/ancestor::div[contains(@class, "BurgerIngredients_ingredients__item")]')

    # Детали ингредиента (модальное окно)
    INGREDIENT_DETAILS_MODAL_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.CSS_SELECTOR, '.Modal_modal__close')

    # Зона конструктора
    BURGER_CONSTRUCTOR_AREA = (By.CSS_SELECTOR, '.BurgerConstructor_burger__wrapper')
    TOP_BUN_IN_CONSTRUCTOR = (By.CSS_SELECTOR, '.BurgerConstructor_burger__list > div:first-child .constructor-element__row')
    BOTTOM_BUN_IN_CONSTRUCTOR = (By.CSS_SELECTOR, '.BurgerConstructor_burger__list > div:last-child .constructor-element__row')
    FILLING_IN_CONSTRUCTOR = (By.CSS_SELECTOR, '.BurgerConstructor_scroll__list .constructor-element')

    # Кнопка оформления заказа
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Модальное окно с номером заказа
    ORDER_NUMBER_MODAL_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title")]') # Общий заголовок, содержащий номер заказа
    ORDER_NUMBER_TEXT = (By.CSS_SELECTOR, '.Modal_modal__title') # Текст с номером заказа

    # Первые ингредиенты каждого типа для создания заказа
    FIRST_BUN = (By.XPATH, '//span[text()="Булки"]/ancestor::div[contains(@class, "tab_tab")]/..//a[1]')
    FIRST_SAUCE = (By.XPATH, '//span[text()="Соусы"]/ancestor::div[contains(@class, "tab_tab")]/..//a[1]')
    FIRST_FILLING = (By.XPATH, '//span[text()="Начинки"]/ancestor::div[contains(@class, "tab_tab")]/..//a[1]')

    # Информация о заказе
    ORDER_NUMBER = (By.CSS_SELECTOR, '.order-number')
    ORDER_SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "order-success")]')

    # Активные вкладки
    BUNS_TAB_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]//span[text()="Булки"]')
    SAUCES_TAB_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]//span[text()="Соусы"]')
    FILLINGS_TAB_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]//span[text()="Начинки"]')

    # Секции ингредиентов
    BUNS_SECTION = (By.XPATH, '//h2[text()="Булки"]/following-sibling::ul[contains(@class, "BurgerIngredients_ingredients__list")]')
    SAUCES_SECTION = (By.XPATH, '//h2[text()="Соусы"]/following-sibling::ul[contains(@class, "BurgerIngredients_ingredients__list")]')
    FILLINGS_SECTION = (By.XPATH, '//h2[text()="Начинки"]/following-sibling::ul[contains(@class, "BurgerIngredients_ingredients__list")]')

    # Детали ингредиента в модальном окне
    INGREDIENT_DETAILS_CONTENT = (By.CSS_SELECTOR, '.Modal_modal__content')

    # Кнопки
    SUBMIT_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS"]')
    SUBMIT_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    # Поля ввода
    EMAIL_INPUT = (By.XPATH, '//input[@type="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')

    # Секции конструктора
    CONSTRUCTOR = (By.CLASS_NAME, 'BurgerConstructor_basket__29Cd7')
    ORDER_FEED = (By.CLASS_NAME, 'OrderFeed_orderFeed__1xqXP')

    # Модальные окна
    INGREDIENT_DETAILS_MODAL = (By.CLASS_NAME, 'Modal_modal__contentBox__3gP0S')
    ORDER_MODAL = (By.CLASS_NAME, 'Modal_modal__contentBox__3gP0S')

    # Элементы модального окна ингредиента
    INGREDIENT_MODAL_TITLE = (By.CLASS_NAME, 'Modal_modal__title__2L7m-')
    INGREDIENT_MODAL_IMAGE = (By.CLASS_NAME, 'Modal_modal__image__2L7m-')
    INGREDIENT_MODAL_DESCRIPTION = (By.CLASS_NAME, 'Modal_modal__description__2L7m-')
    INGREDIENT_MODAL_NUTRITION = (By.CLASS_NAME, 'Modal_modal__nutrition__2L7m-')
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS')

    # Элементы модального окна заказа
    ORDER_MODAL_TITLE = (By.CLASS_NAME, 'Modal_modal__title__2L7m-')
    ORDER_MODAL_NUMBER = (By.CLASS_NAME, 'Modal_modal__number__2L7m-')
    ORDER_MODAL_STATUS = (By.CLASS_NAME, 'Modal_modal__status__2L7m-')
    ORDER_MODAL_INGREDIENTS = (By.CLASS_NAME, 'Modal_modal__ingredients__2L7m-')
    ORDER_MODAL_TOTAL = (By.CLASS_NAME, 'Modal_modal__total__2L7m-')
    ORDER_MODAL_CLOSE_BUTTON = (By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS')

    # Ингредиенты
    INGREDIENT_DRAG_HANDLE = (By.CLASS_NAME, 'BurgerIngredient_ingredient__1TVf6')
