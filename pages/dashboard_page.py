from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_home(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Home']/parent::a"))
        ).click()

        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Home']"))
        )