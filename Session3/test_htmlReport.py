import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver= None

def setup_module(module):
    global driver
    serv_obj=Service("/home/s/Downloads/chromedriver_linux64/chromedriver")
    driver = webdriver.Chrome(service=serv_obj)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url=="https://www.google.com/"