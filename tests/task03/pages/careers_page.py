from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    def is_opened(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Careers"))
        return "Careers" in self.driver.title

    def locations_block_is_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'locations')]"))
        ).is_displayed()

    def teams_block_is_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'teams')]"))
        ).is_displayed()

    def life_at_insider_block_is_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'life-insider')]"))
        ).is_displayed()