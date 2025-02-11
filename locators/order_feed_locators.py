from selenium.webdriver.common.by import By

class OrderFeedLocators:

    # Найти кнопку заказа
    BUTTON_USER_ORDER = (By.XPATH, "//*[contains(@class, 'OrderHistory_listItem__2x95r')]")

    # Найти всплывающее окно
    WINDOW_ORDER = (By.XPATH, "//*[contains(@class, 'text text_type_main-medium')]")

    # НАйти id всех заказов
    ALL_ID_ORDERS = (By.XPATH, "//*[contains(@class, 'text text_type_main-medium')]/../..//*[contains(@class, 'OrderHistory_textBox__3lgbs')]")

    # Найти количество всех заказов
    QUANTITY_ORDER_ALL = (By.XPATH, "//*[text() = 'Выполнено за все время:']/following::*[@class][1]")

    # Найти количество заказов за сегодня
    QUANTITY_ORDER_TODAY = (By.XPATH, "//*[text() = 'Выполнено за сегодня:']/following::*[@class][1]")

    # Найти все заказы в работе
    ID_ORDER_WORK = (By.XPATH, "//*[text() = 'В работе:']/following::li[@class][6]")

