import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")   # required for CI
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")

    assert login.is_logged_in(), "Login failed!"

    return driver