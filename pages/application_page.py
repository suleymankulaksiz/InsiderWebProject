import pytest
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class Application(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
   
    def verify_redirect_to_lever_application_form_page(self,assert_url):
        self.switch_to_window(2)
        assert assert_url in self.driver.current_url, f"Expected '{assert_url}' to be in '{self.driver.current_url}'"
        self.take_screenshot("verifyLeverApplicationPageOpened.png")