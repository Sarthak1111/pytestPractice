import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param=="chrome":
        serv_obj = Service("/home/s/Downloads/chromedriver_linux64/chromedriver")
        driver = webdriver.Chrome(service=serv_obj)
    if request.param=="firefox":
        pass
    request.cls.driver= driver
    yield
    driver.close()
