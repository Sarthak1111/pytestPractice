#install pytet-xdist

import pytest
from selenium import webdriver


def test_3():
    assert False

@pytest.mark.login
def test_login():
    assert 100==1002

def test_gmail():
    driver=webdriver.Chrome('/home/s/Downloads/chromedriver_linux64/chromedriver')
    driver.implicitly_wait(10)
    driver.get("https://mail.google.com/")
    driver.quit()

def test_fb():
    driver=webdriver.Chrome('/home/s/Downloads/chromedriver_linux64/chromedriver')
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    driver.quit()

def test_flikart():
    driver=webdriver.Chrome('/home/s/Downloads/chromedriver_linux64/chromedriver')
    driver.implicitly_wait(10)
    driver.get("https://www.flipkart.com/")
    driver.quit()