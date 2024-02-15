import re
import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
import urllib.request


class SbisPageLocators:
    TENSOR_IMG = (By.XPATH, "//a[contains(@class, 'sbisru-Contacts__logo-tensor')]")
    CONTACT_URL = 'https://sbis.ru/contacts'
    CHENGE_REGION_BTN = (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text sbis_ru-link')]")
    REGIONS_BTNS = (By.XPATH, "//span[contains(@class, 'sbis_ru-link')]")
    PARTNERS_BLOCK = (By.XPATH, "//div[contains(@class, 'sbis_ru-container')]")
    FOOTER_LINK_DOWNLOAD = (By.LINK_TEXT, TestData.FOOTER_DOWNLOAD_TITLE)
    PLUGIN_TAB = (By.XPATH, "//div[contains(@data-id, 'plugin')]/div")
    LINK = (By.XPATH, "//a[contains(@class, 'sbis_ru-DownloadNew-loadLink__link js-link')]")
    COOCKIE_CLOSE = (By.XPATH, "//div[contains(@class, 'sbis_ru-CookieAgreement__close')]")


class SbisPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://sbis.ru/'

    def goto_contact(self):
        self.get(SbisPageLocators.CONTACT_URL)

    def click_tensor_img(self):

        img = self.find_element(SbisPageLocators.TENSOR_IMG)
        self.click_to_element(img)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # происходит редирект, нужно переключить окно

    def check_region_and_partners(self):
        region = self.find_element(SbisPageLocators.REGIONS_BTNS).text.split(' ')[0]
        if self.driver.title.find(region) != -1:
            if self.is_enabled(SbisPageLocators.PARTNERS_BLOCK):
                return True
        return False

    def select_region(self, region):
        self.find_element(SbisPageLocators.CHENGE_REGION_BTN).click()
        for region_span in self.find_elements(SbisPageLocators.REGIONS_BTNS):
            if region_span.text.find(region) != -1:
                self.click_to_element(region_span)

    def click_download_sbis_on_footer(self):

        try:
            coockie = self.find_element(
                SbisPageLocators.COOCKIE_CLOSE)  # форма с принятием куки, закрываю, скролл не работает
            self.click_to_element(coockie)
        except:
            ...
        down_link = self.find_element(SbisPageLocators.FOOTER_LINK_DOWNLOAD)
        self.click_to_element(down_link)

    def select_product(self):
        tab = self.find_element(SbisPageLocators.PLUGIN_TAB)
        self.click_to_element(tab)

    def download_sbis(self):
        link = self.find_elements(SbisPageLocators.LINK)[0]
        size_file = re.search('(\d.\d{2})', link.text).group(0)
        destination = '../Tests/test.exe'
        url = link.get_attribute('href')
        urllib.request.urlretrieve(url, destination)
        return size_file
