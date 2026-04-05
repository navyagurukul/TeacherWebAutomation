from pages.login_page import LoginPage
from pages.lesson_plan_page import LessonPlanPage

def test_lesson_pdf(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")

    lesson_plan_page = LessonPlanPage(driver)

    assert lesson_plan_page.get_pdf_count() > 0