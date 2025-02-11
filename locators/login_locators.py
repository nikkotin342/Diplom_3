from selenium.webdriver.common.by import By

class LoginLocators:

    # Найти кнопку восстановить пароль
    SEARCH_RECOVER_PASSWORD = (By.XPATH, ".//a[contains(text(), 'Восстановить пароль')]")

    # Поле EMAIL
    FIELD_EMAIL = (By.XPATH, "//*[contains(@name,'name')]")

    # Поле PASSWORD
    FIELD_PASSWORD = (By.XPATH, "//*[contains(@name,'Пароль')]")

    # Кнопка ВОЙТИ
    BUTTON_ENTER = (By.XPATH, "//*[contains(@class, 'button_button__33qZ0') and text() = 'Войти']")

    # Кнопка ОФОРМИТЬ ЗАКАЗ
    BUTTON_DESIGNER = (By.XPATH, "//*[contains(@class,'button_button__33qZ0') and text() = 'Оформить заказ']")

    # История заказов
    HISTORY_ORDER = (By.XPATH, "//*[contains(@class,'Account_link__2ETsJ text text_type_main-medium') and text() = 'История заказов']")

    # Кнопка выйти из аккаунта
    EXIT_ACCOUNT = (By.XPATH, "//*[contains(@class,'Account_button__14Yp3 text') and text() = 'Выход']")

    # Локатор id заказа
    ID_ORDER = (By.XPATH, "//*[contains(@class,'text text_type_digits-default')]")

