import pytest
from constants.quality_assurance_locator import *
from pages.base_page import *

@pytest.mark.usefixtures("setup")
class QualityAssurance(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
   
    def open_new_window(self,url):
        self.new_window(url)
    
    def verify_qa_page_opened(self, expected_url):
        assert expected_url in self.driver.current_url, f"Expected '{expected_url}' to be in '{self.driver.current_url}'"
        self.take_screenshot("verifyQAPageOpened.png")
        
    def click_see_all_qa_jobs_button(self):
        self.click_element(SEE_ALL_QA_JOBS_BUTTON)
    
    def verify_all_qa_jobs_page_opened(self,expected_url):
        assert expected_url in self.driver.current_url, f"Expected '{expected_url}' to be in '{self.driver.current_url}'"
        self.take_screenshot("verifyAllQAJobsPageOpened.png")
    
    def select_location_filter(self):
        self.wait_for_text_in_element(LOCATION_TEXT, 'Quality Assurance')
        self.click_element(FILTER_LOCATION)
        self.wait_element_visibility(LOCATION_TEXT_AREA)
        self.click_element(LOCATION_TEXT_AREA)
        
    def verify_filters_selected(self,expected_title,expected_title2):
        self.scroll_down(500)
        filter_location_area = self.wait_element_visibility(FILTER_LOCATION)
        actual_title = filter_location_area.get_attribute('title')
        assert expected_title in actual_title, f"Expected '{expected_title}' text was not found in '{actual_title}'."
        print(f"The text '{expected_title}' was verified within {FILTER_LOCATION}.")

        filter_department_area = self.wait_element_visibility(FILTER_DEPARTMENT)
        actual_title2 = filter_department_area.get_attribute('title')
        assert expected_title in actual_title, f"Expected '{expected_title2}' text was not found in '{actual_title2}'."
        print(f"The text '{expected_title}' was verified within {FILTER_DEPARTMENT}.")
        self.wait_element_visibility(DEPARTMENT_NAME)
        self.take_screenshot("verifyFiltersSelected.png")
            
    def verify_department_name_and_job_title(self, title):
        self.wait_for_text_in_element(DEPARTMENT_NAME,'Quality Assurance')
        departments = self.find_elements(DEPARTMENT_NAME)
        
        for job_deparment in departments:
            department_text = job_deparment.text
            assert title in department_text, f"Expected '{title}' to be in '{department_text}', but it was not found."
        self.take_screenshot("verifyDepartmentName.png")
        self.wait_for_text_in_element(JOB_TITLE,'Quality Assurance')
        job_titles = self.find_elements(JOB_TITLE)
        for job_qa in job_titles:
            job_name_text = job_qa.text
            assert title in job_name_text, f"Expected '{title}' to be in '{job_name_text}', but it was not found."
        self.take_screenshot("verifyJobTitle.png")

    def verify_location_info(self, location_name):
        self.wait_for_text_in_element(LOCATION_INFO,"Istanbul, Turkey")
        elements = self.find_elements(LOCATION_INFO)
        for job_qa in elements:
            location_text = job_qa.text
            assert location_name in location_text, f"Expected '{location_name}' to be in '{location_text}', but it was not found."
        self.take_screenshot("verifyLocationInfo.png")

    def click_view_role_button(self):
        view_role_button = self.find_elements(VIEW_ROLE_BUTTON)
        if len(view_role_button) > 1:
            view_role_button[1].click()