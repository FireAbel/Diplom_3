from selenium.webdriver.common.by import By


class MainPageLocators:
    # Элементы конструктора
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    CONSTRUCTOR_BURGER = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')
    MAKE_BURGER_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients")]/h1')

    # Кнопки навигации
    ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(@class, "button_button") and contains(text(), "Войти")]')

    # Карточки ингредиентов
    BUN_CARD = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    SAUCE_CARD = (By.XPATH, '//img[@alt="Соус Spicy-X"]')
    FILLING_CARD = (By.XPATH, '//img[@alt="Мясо бессмертных моллюсков Protostomia"]')

    # Счетчики ингредиентов
    BUN_COUNTER = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]/preceding-sibling::div/p')
    SAUCE_COUNTER = (By.XPATH, '//img[@alt="Соус Spicy-X"]/preceding-sibling::div/p')
    FILLING_COUNTER = (By.XPATH, '//img[@alt="Мясо бессмертных моллюсков Protostomia"]/preceding-sibling::div/p')

    # Вкладки конструктора
    BUNS_TAB = (By.XPATH, '//span[text()="Булки"]')
    SAUCES_TAB = (By.XPATH, '//span[text()="Соусы"]')
    FILLINGS_TAB = (By.XPATH, '//span[text()="Начинки"]')

    # Локаторы для активных вкладок
    BUNS_TAB_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab_type_current") and .//span[text()="Булки"]]')
    SAUCES_TAB_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab_type_current") and .//span[text()="Соусы"]]')
    FILLINGS_TAB_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab_type_current") and .//span[text()="Начинки"]]')

    # Секции ингредиентов
    BUNS_SECTION = (
    By.XPATH, '//h2[text()="Булки"]/following-sibling::ul[contains(@class, "BurgerIngredients_ingredients__list")]')
    SAUCES_SECTION = (
    By.XPATH, '//h2[text()="Соусы"]/following-sibling::ul[contains(@class, "BurgerIngredients_ingredients__list")]')
    FILLINGS_SECTION = (
    By.XPATH, '//h2[text()="Начинки"]/following-sibling::ul[contains(@class, "BurgerIngredients_ingredients__list")]')

    # Модальные окна
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]')
    INGREDIENT_DETAILS_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_DETAILS_CONTENT = (By.XPATH, '//div[contains(@class, "Modal_modal__content")]')

    # Элементы заказа
    ORDER_ID = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')
    ORDER_STATUS = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ORDER_IDENTIFIER = (By.XPATH, '//p[text()="идентификатор заказа"]')
    LOADING_CHECKBOX = (By.XPATH, '//img[@alt="tick animation"]')

    # Элементы конструктора
    BUN_IN_BURGER = (
    By.XPATH, ".//div[contains(@class, 'pos_top')]//span[contains(text(), 'Флюоресцентная булка R2-D3')]")
    CONSTRUCTOR = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')
    INGREDIENT_DRAG_HANDLE = (By.CLASS_NAME, 'BurgerIngredient_ingredient__1TVf6')
    MAKE_BURGER = (By.XPATH, './/section[contains(@class, "BurgerIngredients")]/h1')

    # Элементы ленты заказов
    ORDER_FEED = (By.CLASS_NAME, 'OrderFeed_orderFeed__1xqXP')

    INGREDIENT_DETAILS_CLOSE_BUTTON = (
    By.XPATH, ".//section[contains(@class, 'Modal_modal_open')]//button[contains(@class, 'close')]")
    CLOSE_ORDER_DETAILS = (By.XPATH, ".//button[contains(@class, 'modal__close__TnseK')]")
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")

    ID_ORDER = (
    By.XPATH, ".//div[contains(@class, 'container__Wo2l')]//h2[contains(@class, 'title_shadow__3ikwq Mod')]")

    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')

    # Модальные окна
    INGREDIENT_MODAL = (By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X')
    # Элементы ингредиентов
    INGREDIENT_MODAL_TITLE = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали')]")

    LOADING_CHECK_BOX = (By.XPATH, ".//img[@alt='tick animation']")
    MODAL_CLOSE_BUTTON = (By.XPATH, './/section[contains(@class, "Modal_modal_open")]//button[contains(@class, "close")]')
    MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_modal_overlay__x2ZCr")]')