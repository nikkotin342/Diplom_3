import allure

from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


@allure.title("Страница восстановленя пароля")
class ForgotPasswordPage(BasePage):

    @allure.step("Пишем в поле для восстановления пароля email")
    def enter_reed_forgot_password_email(self, text):
        self.enter_text(ForgotPasswordLocators.SEARCH_FIELD_FORGOT_PASSWORD_EMAIL, text)

    @allure.step("Кликаем на кнопку восстановить")
    def click_recover_password(self):
       self.click_text_button(ForgotPasswordLocators.SEARCH_RECOVER_PASSWORD)

    @allure.step("Ожидание когда появится поле куда вводить пароль")
    def without_element(self):
        self.find_element_visual(ForgotPasswordLocators.SEARCH_FIELD_PASSWORD)

    @allure.step("Кликаем на поле куда вводить пароль")
    def enter_password(self):
        self.click_text_button(ForgotPasswordLocators.SEARCH_FIELD_PASSWORD)

    @allure.step("Ввод пароля")
    def set_new_password(self, password):
        self.enter_text(ForgotPasswordLocators.SET_NEW_PASSWORD, password)

    @allure.step("Получаем родительский класс поля с паролем")
    def get_parent_class_password_field(self):
        return self.find_element(ForgotPasswordLocators.PASSWORD_FIELD_PARENT)

    @allure.step("Присваиваем переменной родительский класс поля Пароль")
    def assign_parent_class_password_by_variable(self):
        return self.find_element(ForgotPasswordLocators.HIGHLIGHTED_PASSWORD_FIELD)






