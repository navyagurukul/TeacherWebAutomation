import pytest
from pages.login_page import LoginPage

@pytest.mark.order(1)
def test_login_valid(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")

    assert login.is_logged_in()