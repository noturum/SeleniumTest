import time

import selenium.webdriver.support.select
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
    Базовый клас для всех страниц, здесь определены общие методы,
    которые будут использоваться в дочерних классах.
    """

    def __init__(self, driver):

        self.url = None
        self.driver = driver
        self.wait = wait(self.driver, 10)

    def click_to_element(self, element):
        """
        Совершает нажатие на элемент
        :param element:
        :exception ElementClickInterceptedException: может образоваться, если елемент перекрыт другим
        """
        try:
            element.click()
        except ElementClickInterceptedException as e:
            print(e)
            ActionChains(self.driver).scroll_by_amount(0, 100).move_to_element(element).click(element).perform()

    def get(self, url):
        browser = self.driver.get(url)

        return browser

    def find_elements(self, by_localtor):
        return self.wait.until(ES.visibility_of_any_elements_located(by_localtor))

    def find_element(self, by_locator):
        return self.wait.until(ES.visibility_of_element_located(by_locator))

    def is_enabled(self, by_locator: tuple[str, str]):
        obj = self.wait.until(ES.visibility_of_element_located(by_locator))
        return bool(obj)
