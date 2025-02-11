from selenium.webdriver.common.by import By

class ForgotPasswordLocators:

    # Найти поле куда вводить email
    SEARCH_FIELD_FORGOT_PASSWORD_EMAIL = (By.XPATH, ".//input[contains(@name,'name')]")

    # Найти кнопку восстановить
    SEARCH_RECOVER_PASSWORD = (By.XPATH, ".//*[text()='Восстановить']")

    # Глазочек в поле ввести пароль
    SEARCH_FIELD_PASSWORD = (By.XPATH, '//div[contains(@class, "input__icon input__icon-action")]')

    SET_NEW_PASSWORD = (By.XPATH,
                        ".//input[@class='text input__textfield text_type_main-default' and @type= 'password']")


    PASSWORD_FIELD_PARENT = (By.XPATH, ".//input[contains(@type,'text')]/parent::div")

    # Подсвеченное поле пароля
    HIGHLIGHTED_PASSWORD_FIELD = (
        By.XPATH,
        ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
