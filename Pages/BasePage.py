import selenium.webdriver.support.select
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Keys
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
        self.wait=wait(self.driver,5)


    def click_to_element(self,element):
        """

        :param element:
        :return:
        """
        try:
            element.click()
        except ElementClickInterceptedException as e:
            ActionChains(self.driver).scroll_by_amount(0,100).perform()
            ActionChains(self.driver).click(element).perform()

    def move_to_element(self,obj):
        ActionChains(self.driver).move_to_element(obj).perform()
    def get(self,url):
        return self.driver.get(url)
    def find_elements(self,by_localtor):
        return self.wait.until(ES.visibility_of_all_elements_located(by_localtor))
    def find_element(self,by_locator):
        return self.wait.until(ES.visibility_of_element_located(by_locator))
    def is_enabled(self,by_locator: tuple[str, str]):
        obj=self.wait.until(ES.visibility_of_element_located(by_locator))
        return bool(obj)
