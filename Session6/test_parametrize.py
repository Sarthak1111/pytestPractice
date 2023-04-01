import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class Basetest():
    pass

class Testhubspot(Basetest):
    @pytest.mark.parametrize(
                                "username, password"
                                [
                                    ("saru@gmail.com", "asd123"),
                                    ("cool@gmail.com", "pad123"),
                                ]
                            )
    def test_login(self, username, password):
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID,"username").send_keys("username")
        time.sleep(3)
        self.driver.find_element(By.ID,"password").send_keys("password")
        time.sleep(3)