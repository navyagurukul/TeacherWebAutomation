from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LessonPlanPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_lesson_tab(self):
        tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Lesson Plan']/parent::a"))
        )
        tab.click()

    def get_pdf_count(self):
        pdfs = self.driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'.pdf')] | "
            "//img[contains(@src,'pdf')] | "
            "//span[contains(@class,'pdf')] | "
            "//i[contains(@class,'pdf')] | "
            "//img[contains(@class,'css-9pa8cd')]"
        )
        return len(pdfs)

    def click_pdf(self):
        pdfs = self.get_pdf_elements()
        if pdfs:
            pdfs[0].click()
            return True
        return False

    def get_pdf_elements(self):
        return self.driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'.pdf')] | "
            "//img[contains(@src,'pdf')] | "
            "//img[contains(@class,'css-9pa8cd')]"
        )

    def click_video(self):
        videos = self.driver.find_elements(
            By.XPATH,
            "//button[contains(.,'Video') or contains(.,'Speaking')]"
        )
        if videos:
            videos[0].click()
            return True
        return False