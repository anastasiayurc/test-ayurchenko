from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.careers_page import CareersPage

class HomePage:
    URL = "https://useinsider.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Insider"))
        return "Insider" in self.driver.title

    def go_to_careers(self):
        company_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Company')]"))
        )
        ActionChains(self.driver).move_to_element(company_menu).perform()
        careers_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Careers')]"))
        )
        careers_link.click()
        return CareersPage(self.driver)