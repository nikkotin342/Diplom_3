import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


@allure.title("Главная страница")
class MainPage(BasePage):

    @allure.step("Клик по кнопке личный кабинет")
    def click_personal_account(self):
        self.click_text_button(MainPageLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Прочитать что написано на кнопке на главном экране")
    def button_place(self):
        return self.add_text(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step("Клик по кнопке конструктор")
    def click_button_constructor(self):
        self.click_text_button(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Клик по кнопке лета заказов")
    def click_order_feed(self):
        self.click_text_button(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step("Клик по булке")
    def click_bulka(self):
        self.click_text_button(MainPageLocators.BUTTON_BULKA)

    @allure.step("Клик по закрытию булки")
    def click_exit_bulka(self):
        self.click_text_button(MainPageLocators.EXIT_WINDOW_BULKA)

    @allure.step("Найти в дереве всплывающее окно")
    def check_window_bulka(self):
        if self.find_element_visual(MainPageLocators.WINDOW_BULKA):
            return True
        else:
            return False

    @allure.step("Проверка что не найдет в дереве")
    def check_exit_window_bulka(self):
        self.find_element_invisual(MainPageLocators.WINDOW_BULKA).is_displayed()

    @allure.step("Перертаскивание элемента")
    def drag_and_drop_main(self):
        source_element = self.wait_and_find_element(MainPageLocators.BUTTON_BULKA)
        target_element = self.wait_and_find_element(MainPageLocators.FIELD_BULKA)
        self.drag_and_drop(source_element, target_element)

    @allure.step("Прочитать заначение каунтера")
    def caunter_text(self):
        return self.add_text(MainPageLocators.CAUNTER_ELEMENTS)

    @allure.step("Клик по кнопке оформить заказ")
    def click_place_an_order(self):
        self.click_text_button(MainPageLocators.BUTTON_DESIGNER)

    @allure.step("Прочитать текст у всплывающего окна при оформлении заказа")
    def text_place_an_order(self):
        return self.add_text(MainPageLocators.PLACE_AN_ORDER)

    @allure.step("Клик по кнопке закрытия окна о оформлении заказа")
    def click_exit_window_order(self):
        return self.click_text_button(MainPageLocators.EXIT_WINDOW_ORDER)

    @allure.step("найти id моего заказа")
    def check_num_order(self):
        return self.add_text(MainPageLocators.ID_MY_ORDER)







