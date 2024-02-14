import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
class SbisPageLocators:
    TENSOR_IMG=(By.CLASS_NAME,'sbisru-Contacts__logo-tensor mb-12')
    CONTACT_URL='https://sbis.ru/contacts'
    CHENGE_REGION_BTN = (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text sbis_ru-link')]")
    REGIONS_BTNS = (By.XPATH, "//span[contains(@class, 'sbis_ru-link')]")
    PARTNERS_BLOCK = (By.XPATH,"//div[contains(@class, 'sbis_ru-container')]")
    FOOTER_LINK_DOWNLOAD=(By.LINK_TEXT,TestData.FOOTER_DOWNLOAD_TITLE)


class SbisPage(BasePage):


    def __init__(self,driver):
        super().__init__(driver)
        self.url='https://sbis.ru/'
    def goto_contact(self):
        self.get(SbisPageLocators.CONTACT_URL)
    def click_tensor_img(self):
        img=self.find_element(SbisPageLocators.TENSOR_IMG)
        self.click_to_element(img)
    def check_region_and_partners(self):
        region=self.find_element(SbisPageLocators.REGIONS_BTNS).text.split(' ')[0]
        if self.driver.title.find(region)!=-1:
            if self.is_enabled(SbisPageLocators.PARTNERS_BLOCK):
                return True
        return False
    def select_region(self,region):
        self.find_element(SbisPageLocators.CHENGE_REGION_BTN).click()
        for region_span in self.find_elements(SbisPageLocators.REGIONS_BTNS):
            if region_span.text.find(region)!=-1:
                self.click_to_element(region_span)

    def click_download_sbis_on_footer(self):
        self.get(self.url)
        down_link=self.find_element(SbisPageLocators.FOOTER_LINK_DOWNLOAD)
        self.click_to_element(down_link)


    def select_product(self):
        ...
    def download_sbis(self):
        ...


import selenium.webdriver
a=SbisPage(selenium.webdriver.Chrome())
a.click_download_sbis_on_footer()

