from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.open_positions_page import OpenPositionsPage

class QACareersPage:
    URL = "https://useinsider.com/careers/quality-assurance/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_see_all_qa_jobs(self):
        see_all_jobs_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'See all QA jobs')]"))
        )
        see_all_jobs_btn.click()
        return OpenPositionsPage(self.driver)