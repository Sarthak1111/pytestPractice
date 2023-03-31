import pytest

def test_1():
    assert False

@pytest.mark.login
def test_login():
    assert "hey"