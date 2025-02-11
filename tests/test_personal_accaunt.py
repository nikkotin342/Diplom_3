import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage

from helpers.url import *

@allure.story('Личный кабинет')
class TestPasswordRecovery:

    @allure.title('Переход по клику личный кабинет и авторизация')
    def test_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.entering_a_email()
        login_page.entering_a_password()
        login_page.click_button_entrance()
        login_page.without_element_order()
        assert main_page.button_place() == 'Оформить заказ'

    @allure.title('Переход на вкладку история заказов')
    def test_history_order(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.entering_a_email()
        login_page.entering_a_password()
        login_page.click_button_entrance()
        login_page.without_element_order()
        main_page.click_personal_account()
        login_page.click_history_order()
        assert driver.current_url == f'{BASE_URL}{ORDER_HISTORY}'

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.entering_a_email()
        login_page.entering_a_password()
        login_page.click_button_entrance()
        login_page.without_element_order()
        main_page.click_personal_account()
        login_page.click_exir_account()
        login_page.without_element_entrance()
        assert driver.current_url == f'{BASE_URL}{LOGIN}'