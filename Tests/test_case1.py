from Pages.TensorPage import TensorPage
from Pages.SbisPage import SbisPage
from Config.config import TestData
import os
def test_case1(webdriver):
    tensor=TensorPage(webdriver)
    sbis=SbisPage(webdriver)
    sbis.get(sbis.url)
    sbis.goto_contact()
    sbis.click_tensor_img()
    tensor.click_about()
    check_img=tensor.check_wh_img()
    assert check_img

def test_case2(webdriver):
    sbis = SbisPage(webdriver)
    sbis.goto_contact()
    sbis.check_region_and_partners()
    sbis.select_region(TestData.TEST_REGION_TITLE)
    sbis.check_region_and_partners()
def test_case3(webdriver):
    sbis = SbisPage(webdriver)
    sbis.get(sbis.url)
    sbis.click_download_sbis_on_footer()
    sbis.select_product()
    size=sbis.download_sbis()
    fact_size=round(os.path.getsize('./test.exe')/(1024*1024), 2)
    assert float(size)==fact_size , fact_size

