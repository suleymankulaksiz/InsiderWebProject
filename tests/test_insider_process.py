from time import sleep
import pytest
import allure
from pages.home_page import HomePage
from pages.careers_page import Careers
from pages.quality_assurance_page import QualityAssurance
from pages.application_page import Application

@pytest.mark.usefixtures("setup")
class TestProcess:
    @allure.title('Insider sayfasına gidilerek Quality Assurance İstanbul pozisyonuna ait başvuru sayfasının açıldığı kontrol edilecektir')
    def test_insider_website(self):
        # Anasayfa işlemleri
        with allure.step('Verify the homepage is opened.'):
            home_page = HomePage(self.driver)
            home_page.verify_homepage_opened("https://useinsider.com/")                              #Anasayfanın açıldığı doğrulanır.
        with allure.step('Accept cookies.'):
            home_page.accept_cookies()                                                               #Çerezler kabul edilir.
        with allure.step('The Company dropdown menu is opened.'):
            home_page.click_dropdown_company()                                                       #Company tıklanır ve dropdown açılır.
        with allure.step('Verify that the Company dropdown is opened.'):
            home_page.verify_dropdown_company_opened("true")                                         #Dropdown açıldığı kontrol edilir.
        with allure.step('Click on the Careers button.'):
            home_page.click_careers_button()                                                         #Careers butonuna tıklanır.

        # Kariyerler sayfası işlemleri
        with allure.step('Verify that the Careers page is opened.'):
            careers = Careers(self.driver)
            careers.verify_careers_page_opened("https://useinsider.com/careers/")                    #Careers sayfasının açıldığı kontrol edilir.
        with allure.step('Verify that the team block is visible and there are 15 items.'):
            careers.verify_teams_block_is_visible("See all teams", 15)                               #Teams bloğunun göründüğü ve toplam team sayısı kontrol edilir.
        with allure.step('Verify that the location block are visible.'):
            careers.verify_location_block_is_visible("Our Locations")                                #Location bloğunun göründüğü kontrol edilir.
        with allure.step('Verify that the Life at Insider block are visible.'):
            careers.verify_life_at_insider_block_is_visible("Life at Insider")                       # Life at Insider bloğunun göründüğü kontrol edilir.
    
        # QA sayfası işlemleri
        with allure.step('A new window opens the Quality Assurance page.'):
            qa = QualityAssurance(self.driver)
            qa.open_new_window("https://useinsider.com/careers/quality-assurance/")                  #Quality Assurance sayfası yeni pencerede açılır.
        with allure.step('Verify that the Quality Assurance page is opened.'):
            qa.verify_qa_page_opened("careers/quality-assurance/")                                   #Quality Assurance sayfasının açıldığı kontrol edilir.
        with allure.step("Click on the 'See All QA Jobs' button."):
            qa.click_see_all_qa_jobs_button()                                                        #'See All QA Jobs' butonuna tıklanır.
        with allure.step('Verify that the All QA Jobs page is opened.'):
            qa.verify_all_qa_jobs_page_opened("department=qualityassurance")                         # All Jobs QA sayfasının açıldığı kontrol edilir.
        with allure.step("Select 'Istanbul, Turkey' as the location filter."):
            qa.select_location_filter()                                                              #'Istanbul,Turkey' lokasyon filtresi seçilir.
        with allure.step("Verify that 'Istanbul, Turkey' is selected as the location filter."):
            qa.verify_filters_selected("Istanbul, Turkey", "Quality Assurance")                      #'Istanbul,Turkey filtresinin seçildiği kontrol edilir.
        with allure.step("Verify that the department name and job title are 'Quality Assurance'."):
            qa.verify_department_name_and_job_title("Quality Assurance")                             #Departman ve İş ünvanı 'Quality Assurance' içeridiği kontrol edilir.
        with allure.step("Verify that the location information is 'Istanbul, Turkey'."):
            qa.verify_location_info("Istanbul, Turkey")                                              #Lokasyonun 'Istanbul,Turkey' seçildiği kontrol edilir.
        with allure.step("Click on the 'View Role' button."):
            qa.click_view_role_button()                                                              #'View Role' butonuna tıklanır.
        
        # Başvuru sayfası işlemleri
        with allure.step('Verify that the user is redirected to the job application form.'):
            app = Application(self.driver)
            app.verify_redirect_to_lever_application_form_page("jobs.lever.co/useinsider")           #İş başvuru sayfasının açıldığı kontrol edilir.