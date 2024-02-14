import pytest,os
from selenium.webdriver import Chrome,ChromeOptions

@pytest.fixture(scope='session')
def webdriver():
    options=ChromeOptions()
    prefs={"download.default_directory":os.getcwd()+'\\..\\Tests'}
    options.add_experimental_option("prefs", prefs);
    driver=webdriver.Chrome()
    yield driver
    driver.quit()