# tests/test_ui.py
import time
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
from utils.ai_reporter import generate_bug_report  

def test_valid_login():
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("John Doe", "ThisIsNotAPassword")
    time.sleep(3)
    
    assert "appointment" in driver.current_url.lower()
    driver.quit()

def test_past_date_booking_bug():
   
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("John Doe", "ThisIsNotAPassword")
    time.sleep(3)
    
    appointment_page = AppointmentPage(driver)
    appointment_page.book_appointment("Hongkong CURA Healthcare Center", "01/01/2020", "Testing Past Date Bug")
    time.sleep(5) 
    
    current_url = driver.current_url.lower()
    driver.quit()
    
    try:
        assert "summary" not in current_url, "BUG DETECTED: System accepted a past date and redirected to summary page!"
    except AssertionError as e:
        generate_bug_report(str(e))
        raise e  