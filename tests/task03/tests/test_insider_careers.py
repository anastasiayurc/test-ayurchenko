import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_careers_page import QACareersPage
from pages.open_positions_page import OpenPositionsPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(f"screenshots/{name}.png")

def test_insider_qa_careers_flow(driver, request):
    try:
        # Step 1: Visit Insider home page and check
        home = HomePage(driver)
        home.open()
        assert home.is_opened(), "Insider home page did not open."

        # Step 2: Go to Careers and check blocks
        careers = home.go_to_careers()
        assert careers.is_opened(), "Careers page did not open."
        assert careers.locations_block_is_visible(), "Locations block not visible."
        assert careers.teams_block_is_visible(), "Teams block not visible."
        assert careers.life_at_insider_block_is_visible(), "Life at Insider block not visible."

        # Step 3: Go to QA Careers, click See all QA jobs, filter jobs, check jobs list
        qa_careers = QACareersPage(driver)
        qa_careers.open()
        open_positions = qa_careers.click_see_all_qa_jobs()
        open_positions.filter_jobs("Istanbul, Turkey", "Quality Assurance")
        assert len(open_positions.get_job_cards()) > 0, "No jobs listed after filtering."

        # Step 4: Check all jobs' Position, Department, Location
        open_positions.validate_jobs("Quality Assurance", "Quality Assurance", "Istanbul, Turkey")

        # Step 5: Click View Role and check Lever page
        open_positions.click_first_view_role()
        assert open_positions.is_lever_page(), "Did not redirect to Lever application form page."

    except Exception as e:
        browser_name = request.node.callspec.params['driver']
        take_screenshot(driver, f"failure_{browser_name}")
        raise