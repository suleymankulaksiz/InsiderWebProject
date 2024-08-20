from selenium import webdriver
from constants.home_page_locator import *
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.maximize_window()
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()
    
    