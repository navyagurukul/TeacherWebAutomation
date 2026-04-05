import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import os
from datetime import datetime


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")

    assert login.is_logged_in()
    return driver


# ✅ Screenshot hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver:
            folder = "screenshots"
            os.makedirs(folder, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            path = os.path.join(folder, file_name)

            driver.save_screenshot(path)
            print(f"\n📸 Screenshot saved: {path}")