from selenium.webdriver.common.by import By

class MainPageLocators:

    # Найти кнопку личный кабинет
    SEARCH_PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//*[contains(@href, '/account')]")

    # Найти кнопку Оформить заказ/войти в аккаунт
    BUTTON_PLACE_ORDER =  (By.XPATH, "//*[contains(@class, 'button_button__33qZ0')]")

    # Найти кнопку Оформить заказт
    BUTTON_DESIGNER = (By.XPATH, "//*[contains(@class,'button_button__33qZ0') and text() = 'Оформить заказ']")

    # Найти кнопку Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, "//*[contains(@class,'AppHeader_header__linkText__3q_va') and text() = 'Конструктор']")

    # Найти кнопку Лента заказов
    BUTTON_ORDER_FEED = (By.XPATH, "//*[contains(@class,'AppHeader_header__linkText__3q_va') and text() = 'Лента Заказов']")

    # Найти кнопку булки
    BUTTON_BULKA = (By.XPATH, "//*[contains(@alt,'Краторная булка N-200i')]")


    # Найти всплывающее окно
    WINDOW_BULKA = (By.XPATH, "//h2[text()='Детали ингредиента']")

    # Найти кнопку закрытия у всплывающего окна
    EXIT_WINDOW_BULKA = (By.XPATH, "//*[contains(@class,'Modal_modal__close_modified__3V5XS')]")

    # Найти поле куда перетаскивать булочку
    FIELD_BULKA = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    # Найти поле каунтера ингридиента
    CAUNTER_ELEMENTS = (By.XPATH, "//*[contains(@alt, 'Краторная булка N-200i')]/..//*[contains(@class, 'counter_counter__ZNLkj')]")

    # Локатор оформленного заказа
    PLACE_AN_ORDER = (By.XPATH, "//*[contains(@class, 'undefined text text_type_main-small')]")

    # Найти кнопку закрытия сообщения о оформлении заказа
    EXIT_WINDOW_ORDER = (By.XPATH, "//*[contains(@class, 'Modal_modal__close_modified__3V5XS')]")

    # Найти id моего заказа
    ID_MY_ORDER = (By.XPATH, "//*[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

    # Проверка что окно закзка прогрузилось
    ORDER_WINDOW_APLOAD = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened__3ISw4')]")

