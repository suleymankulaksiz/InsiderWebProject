from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from constants.home_page_locator import *
from selenium.webdriver.common.action_chains import ActionChains
import os
import allure
import time

class PageBase:
    def __init__(self, driver):
        self.driver = driver
    
    #Verilen locator görünür olmasını bekler.   
    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
    
    #Verilen locator için tıklama işlemini gerçekleştirir.    
    def click_element(self,locator):
        self.wait_element_visibility(locator).click()
    
    #Verilen locator için yazı girme işlemini gerçekleştirir.
    def send_keys_element(self,locator,text):
        self.wait_element_visibility(locator).send_keys(text)
      
    #Çerezleri kabul etme işlemini gerçekleştirir.    
    def accept_cookies(self):
        self.click_element(COOKIES)
    
    #Verilen locator'ı sayfa içinde bulma işlemini gerçekleştirir.
    def find_element(self,locator):
        return self.driver.find_element(*locator)
    
    #Verilen liste locator'ı sayfa içinde bulma işlemini gerçekleştirir. 
    def find_elements(self,locator):
        return self.driver.find_elements(*locator)
    
    #Verilen locator'ı sayfa içinde çift tıklayarak işlemini gerçekleştirir.
    def doubleclick_element(self,locator):
        element = self.wait_element_visibility(locator)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
    
    #Verilen screenshot ismiyle ekran görüntüsü alır ve allure framework'a ekler.
    def take_screenshot(self, screenshotName):
        time.sleep(0.8)
        file_path = os.path.join("screenshot", screenshotName)
        self.driver.save_screenshot(file_path)
        with open(file_path, 'rb') as f:
            allure.attach(f.read(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
    
    #Pixels olarak belirtilen değişkene değer ataması yapılarak sayfada scroll yapılma işlemini gerçekleştirir.    
    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
    
    #Otomasyon sırasında url ile belirtilen alana değer girilerek yeni bir pencere açma işlemini gerçekleştirir.
    def new_window(self,url):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(f"{url}")
    
    #Locator'ı verilen konumda görünür olmasını 15 saniye bekler ve ardından içindeki texti alır.
    def wait_for_text_in_element(self, locator, text, timeout=15):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(expected_conditions.visibility_of_element_located(locator))
            wait.until(expected_conditions.text_to_be_present_in_element(locator, text))
            print(f'The text "{text}" is visible within {locator}.')
        except Exception as message_text:
            print(f"An error occurred: {message_text}")
    
    #Verilen sayfaya geçiş işlemini gerçekleştirir. Page değişkenine geçilmek istenen sayfa nosu verilerek yapılır unutmayın 1. pencere için [0]
    def switch_to_window(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])