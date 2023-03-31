import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver=None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("========hey init===========")
    serv_obj=Service("/home/s/Downloads/chromedriver_linux64/chromedriver")
    driver = webdriver.Chrome(service=serv_obj)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    yield
    print("======teardown======")
    driver.quit()

# @pytest.mark.usefixtures(init_driver)
def test_google_title(init_driver):
    assert driver.title == "Google"

#@pytest.mark.usefixtures(init_driver)
def test_curr_url(init_driver):
    assert driver.current_url == "https://www.google.com/"