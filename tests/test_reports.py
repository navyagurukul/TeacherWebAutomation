import pytest
from pages.report_page import ReportPage

@pytest.mark.order(3)
def test_student_report(logged_in_driver):
    report = ReportPage(logged_in_driver)

    report.open_student_report()

    assert report.is_student_report_loaded()