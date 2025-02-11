import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage


@allure.story('Проверка Ленты заказов')
class TestOrderFeed:

    @allure.title('По клику на заказ всплывает окно с деталями')
    def test_click_order_info(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        order_feed.click_order_user()
        assert order_feed.check_window_order() == True

    @allure.title('id из истории заказов отображается в ленте заказов')
    def test_id_order_in_order_feed(self, driver):
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
        main_page.click_exit_window_order()
        main_page.click_personal_account()
        login_page.click_history_order()
        id_order = login_page.add_text_id_order()
        main_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        assert order_feed.id_all_user(id_order) == True

    @allure.title('Увеличение счетчика заказов за все время')
    def test_id_order_in_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        main_page.click_personal_account()
        login_page.entering_a_email()
        login_page.entering_a_password()
        login_page.click_button_entrance()
        login_page.without_element_order()
        main_page.click_order_feed()
        old_order = order_feed.quantity_order_all()
        main_page.click_button_constructor()
        main_page.drag_and_drop_main()
        main_page.click_place_an_order()
        main_page.click_exit_window_order()
        main_page.click_order_feed()
        assert order_feed.quantity_order_all() != old_order

    @allure.title('Увеличение счетчика заказов за сегодня')
    def test_id_order_in_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_site()
        main_page.click_personal_account()
        login_page.entering_a_email()
        login_page.entering_a_password()
        login_page.click_button_entrance()
        login_page.without_element_order()
        main_page.click_order_feed()
        old_order = order_feed.quantity_order_today()
        main_page.click_button_constructor()
        main_page.drag_and_drop_main()
        main_page.click_place_an_order()
        main_page.click_exit_window_order()
        main_page.click_order_feed()
        assert order_feed.quantity_order_today() != old_order

    @allure.title('появление нового заказа в разделе работа')
    def test_id_order_in_order_feed(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.go_to_site()
        main_page.click_personal_account()
        login_page.entering_a_email()
        login_page.entering_a_password()
        login_page.click_button_entrance()
        login_page.without_element_order()
        main_page.drag_and_drop_main()
        main_page.click_place_an_order()
        num_order = main_page.check_num_order()
        main_page.click_exit_window_order()
        main_page.click_order_feed()
        return order_feed.order_in_work(num_order) == True



