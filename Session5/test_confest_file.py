import pytest


@pytest.mark.usefixtures("init_driver")
class BaseClass:
    pass


class Test_childClass(BaseClass):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title=="Google"

    def test_url(self):
        self.driver.get("http://www.google.com")
        assert self.driver.currrent_url=="google.com"