import allure

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


@allure.title("Страница лента заказов")
class OrderFeedPage(BasePage):

    @allure.step("Клик по заказу ")
    def click_order_user(self):
        self.click_text_button(OrderFeedLocators.BUTTON_USER_ORDER)

    @allure.step("Найти в дереве всплывающее окно")
    def check_window_order(self):
        if self.find_element_visual(OrderFeedLocators.WINDOW_ORDER):
            return True
        else:
            return False

    @allure.step("Проверка на то что id моего закакза лежит в списке всех заказов")
    def id_all_user(self, id_my_order):
        elements = self.find_all_elements(OrderFeedLocators.ALL_ID_ORDERS)

        for element in elements:
            if id_my_order == element.text:
                return True
        return True

    @allure.step("Найти количество заказов за все вермя")
    def quantity_order_all(self):
        return self.add_text(OrderFeedLocators.QUANTITY_ORDER_ALL)

    @allure.step("Найти количество заказов за сегодня")
    def quantity_order_today(self):
        return self.add_text(OrderFeedLocators.QUANTITY_ORDER_TODAY)

    @allure.step("Проверка на то что мой заказ лежит в списке заказов в работе")
    def order_in_work(self, id_my_order):
        elements = self.find_all_elements(OrderFeedLocators.ID_ORDER_WORK)

        for element in elements:
            if id_my_order == element.text:
                return True
        return True