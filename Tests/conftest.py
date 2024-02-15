import pytest
from selenium.webdriver import Chrome, ChromeOptions, DesiredCapabilities

""" В этом файле определяются общие фикстуры для использования в методах
pytest
"""
"""yield фикстура для инициализации вебдрайвера, и его освобождении"""


@pytest.fixture(scope='session')
def webdriver():
    driver = Chrome()
    yield driver
    driver.quit()
