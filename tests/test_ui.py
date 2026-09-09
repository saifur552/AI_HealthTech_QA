# tests/test_ui.py
import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
from utils.ai_reporter import generate_bug_report  # AI রিপোর্টার इम्पोर्ट করা হলো

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
    """টেস্ট ২: অতীতের তারিখ দিয়ে বুকিং আটকানো এবং স্বয়ংক্রিয় AI বাগ রিপোর্ট জেনারেট করা"""
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
    
    # টেস্ট ফেইল করলে AI দিয়ে অটোমেটিক বাগ রিপোর্ট জেনারেট করার লজিক
    try:
        assert "summary" not in current_url, "BUG DETECTED: System accepted a past date and redirected to summary page!"
    except AssertionError as e:
        # টেস্ট ফেইল করার কারণটি AI-কে পাঠিয়ে দেওয়া হচ্ছে
        generate_bug_report(str(e))
        raise e  # টেস্টটি যাতে পাইথনের চোখেও ফেইল হিসেবে রেকর্ড থাকে