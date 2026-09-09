# tests/test_ui.py
import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage

def test_valid_login():
    """টেস্ট ১: সঠিকভাবে লগইন হচ্ছে কি না"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("John Doe", "ThisIsNotAPassword")
    time.sleep(3)
    
    assert "appointment" in driver.current_url.lower()
    driver.quit()

def test_past_date_booking_bug():
    """টেস্ট ২: অতীতের তারিখ দিয়ে বুকিং আটকানো (Logical Bug Detection)"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("John Doe", "ThisIsNotAPassword")
    time.sleep(3)
    
    appointment_page = AppointmentPage(driver)
    appointment_page.book_appointment("Hongkong CURA Healthcare Center", "01/01/2020", "Testing Past Date Bug")
    
    # পেজ লোড হওয়ার জন্য ৫ সেকেন্ড অপেক্ষা (যাতে সে ধোঁকা না খায়)
    time.sleep(5) 
    
    current_url = driver.current_url.lower()
    driver.quit()
    
    # SQA লজিক: অতীতের তারিখ দিলে সিস্টেমের বুকিং নেওয়া উচিত না।
    # যদি URL-এর ভেতর 'summary' (অর্থাৎ কনফার্মেশন) চলে আসে, তার মানে ওয়েবসাইটে বাগ আছে!
    assert "summary" not in current_url, "BUG DETECTED: System accepted a past date!"