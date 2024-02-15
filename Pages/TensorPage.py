import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class TensorPageLocators:
    """Класс для локаторов сайта"""
    POWER_IN_PEOPLE_BLOCK = (By.XPATH,
                             "//div[contains(@class, 'tensor_ru-Index__block4-content tensor_ru-Index__card')]")
    WORKING_BLOCK = (By.CLASS_NAME, 'tensor_ru-About__block3-image-wrapper')

    BTN_ABOUT = (By.LINK_TEXT, 'Подробнее')


class TensorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://tensor.ru/'

    def click_about(self):
        block = self.find_element(TensorPageLocators.POWER_IN_PEOPLE_BLOCK)
        self.click_to_element(block.find_element(*TensorPageLocators.BTN_ABOUT))

    def check_wh_img(self):

        last_size = None
        wrappers = self.find_elements(TensorPageLocators.WORKING_BLOCK)
        for div in wrappers:
            img = div.find_element(By.TAG_NAME, 'img')
            if not last_size:
                last_size = img.size
            if last_size != img.size:
                return False
            return True



