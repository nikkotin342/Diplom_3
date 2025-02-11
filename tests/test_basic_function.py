import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage

from helpers.url import *

@allure.story('Проверка базовой функциональности')
class TestBasicFunction:

    @allure.title('Переход по клику на конструктор')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_button_constructor()
        assert driver.current_url == BASE_URL

    @allure.title('Переход по клику на ленту заказов')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed()
        assert driver.current_url == f'{BASE_URL}{ORDER_FEED}'

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_bulka()
        assert main_page.check_window_bulka() == True

    @allure.title('Закрытие окна с деталями')
    def test_click__feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_bulka()
        main_page.click_exit_bulka()
        assert not main_page.check_exit_window_bulka()

    @allure.title('Добавление ингредиента')
    def test_click__feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.drag_and_drop_main()
        assert main_page.caunter_text() == '2'

    @allure.title('Залогиненый пользователь может оформить заказ')
    def test_click__feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.entering_a_email()
        login_page.entering_a_password()
        login_page.click_button_entrance()
        login_page.without_element_order()
        main_page.drag_and_drop_main()
        main_page.click_place_an_order()
        assert main_page.text_place_an_order() == 'Ваш заказ начали готовить'