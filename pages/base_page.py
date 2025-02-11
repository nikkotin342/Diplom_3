from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from helpers.url import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL

    # Зайти на сайт
    def go_to_site(self):
        self.driver.get(self.url)

    # ожидание на то что элемент есть
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    # найтивсех эелементы
    def find_all_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(locator))



    # ожидание на то что элемент виден
    def find_element_visual(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    # ожидание на то что элемент не виден
    def find_element_invisual(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located(locator))

    # Клик по элементу
    def click_to_element(self, locator):
        element = self.find_element_visual(locator)
        element.click()

    # Клик по текстовой кнопке
    def click_text_button(self, locator):
        element = self.find_element_visual(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # Достать url
    def current_url(self):
        return self.driver.current_url

    # Проверка на кликабельность
    def wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))

    # Ввести текст
    def enter_text(self, locator, text):
        element = self.wait_element_clickable(locator)
        element.clear()
        element.send_keys(text)

    # Прочитать текст на элементе
    def add_text(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).text

    def wait_and_find_element(self, locator):
        return self.driver.find_element(*locator)

    # Перетаскивание элемента
    def drag_and_drop(self, source_element, target_element):
        return drag_and_drop(self.driver, source_element, target_element)





