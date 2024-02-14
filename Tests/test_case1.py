from Pages.TensorPage import TensorPage
from Pages.SbisPage import SbisPage
from Config.config import TestData

def test_case1(webdriver):
    tensor=TensorPage(webdriver)
    sbis=SbisPage(webdriver)
    sbis.get(sbis.url)
    sbis.goto_contact()
    sbis.click_tensor_img()
    tensor.get(tensor.url)
    tensor.click_about()

def test_case2(webdriver):
    sbis = SbisPage(webdriver)
    sbis.goto_contact()
    sbis.check_region_and_partners()
    sbis.select_region(TestData.TEST_REGION_TITLE)
    sbis.check_region_and_partners()
def test_case3(webdriver):
    ...
