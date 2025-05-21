from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class OpenPositionsPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_jobs(self, location, department):
        location_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='filter-by-location']"))
        )
        Select(location_dropdown).select_by_visible_text(location)

        department_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='filter-by-department']"))
        )
        Select(department_dropdown).select_by_visible_text(department)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='position-list-item-wrapper']"))
        )

    def get_job_cards(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='position-list-item-wrapper']")

    def validate_jobs(self, position_text, department_text, location_text):
        job_cards = self.get_job_cards()
        assert len(job_cards) > 0, "No jobs found for the selected filters."
        for card in job_cards:
            position = card.find_element(By.XPATH, ".//p[@class='position-title']").text
            department = card.find_element(By.XPATH, ".//span[@class='position-department']").text
            location = card.find_element(By.XPATH, ".//span[@class='position-location']").text
            assert position_text in position, f"Position does not contain '{position_text}': {position}"
            assert department_text in department, f"Department does not contain '{department_text}': {department}"
            assert location_text in location, f"Location does not contain '{location_text}': {location}"

    def click_first_view_role(self):
        view_role_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'View Role')]"))
        )
        view_role_btn.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_lever_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("lever.co")
        )
        return "lever.co" in self.driver.current_url