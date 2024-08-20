import pytest
from constants.home_page_locator import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_homepage_opened(self,assert_url):
        self.take_screenshot("verifyHomepageOpened.png")
        assert assert_url == self.driver.current_url, f"Expected '{assert_url}' to be in '{self.driver.current_url}'"
         
    def click_dropdown_company(self):
        self.click_element(COMPANY)
    
    def verify_dropdown_company_opened(self, expected_value):
        self.take_screenshot("verifyDropDownOpened.png")
        dropdown = self.wait_element_visibility(OPEN_COMPANY)
        actual_value = dropdown.get_attribute("aria-expanded")  
        assert actual_value == expected_value, f"Dropdown did not open with the expected value of {expected_value}, current value: {actual_value}"
        
    def click_careers_button(self):
        self.click_element(CAREERS)