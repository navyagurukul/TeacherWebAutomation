from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get("https://teacher.englishgurukul.in/")

    def login(self, school, phone):
        # Click school dropdown
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[text()='Search your school']")
        )).click()

        # Enter school name
        dropdown = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Type here...']")
        ))
        dropdown.send_keys(school)

        # Select school
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//*[text()='{school}']")
        )).click()

        # Enter phone number
        phone_input = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter your 10 digit mobile number']")
        ))
        phone_input.send_keys(phone)

        # Click login
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[text()='Login']")
        )).click()

        # ✅ IMPORTANT: wait for page to load after login
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Home')]")
        ))

    def is_logged_in(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(text(),'Home')]")
                )
            )
            return True
        except:
            return False