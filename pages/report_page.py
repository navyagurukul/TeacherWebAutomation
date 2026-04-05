from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReportPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    # ===== Student Report =====
    def open_student_report(self):
        student_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Student Report']/parent::a")
            )
        )
        student_tab.click()

        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Student Report']")
            )
        )

    def is_student_report_loaded(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//span[normalize-space()='Student Report']")
                )
            )
            return True
        except:
            return False

    # ===== Optional: Data validation =====
    def get_student_rows_count(self):
        rows = self.driver.find_elements(
            By.XPATH,
            "//table//tr"
        )
        return len(rows)
def wait_for_loader_to_disappear(self):
    try:
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@style,'rgba(0, 0, 0, 0.2)')]")
            )
        )
    except:
        pass