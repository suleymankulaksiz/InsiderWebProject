import pytest
from constants.careers_page_locator import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class Careers(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
   
    def verify_careers_page_opened(self,assert_url):
        assert assert_url == self.driver.current_url, f"Expected '{assert_url}' to be in '{self.driver.current_url}'"
        self.take_screenshot("verifyCareersPageOpened.png")
        
    def verify_teams_block_is_visible(self,expected_text,expected_count):
        self.scroll_down(2300)
        self.take_screenshot("verifyTeamsBlockIsVisible.png")
        teams = self.find_element(TEAMS_BLOCK)
        actual_text = teams.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        self.click_element(ALL_TEAMS_BLOCK)
        self.wait_element_visibility(JOBS_WAIT) 
        job_list = self.find_elements(ALL_JOBS_COUNT)
        testResult = len(job_list) == expected_count
        assert testResult, "The expected result did not match the actual result."
    
    def verify_location_block_is_visible(self,expected_text):
        self.scroll_down(3800)
        self.take_screenshot("verifyLocationBlockIsVisible.png")
        location = self.find_element(LOCATION_BLOCK)
        actual_text = location.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"
        
    def verify_life_at_insider_block_is_visible(self,expected_text):
        self.scroll_down(950)
        self.take_screenshot("verifyLifeAtInsiderBlockIsVisible.png")
        life_at_insider = self.find_element(LIFE_AT_INSIDER_BLOCK)
        actual_text = life_at_insider.text
        assert actual_text == expected_text, f"Expected: '{expected_text}', Found: '{actual_text}'"