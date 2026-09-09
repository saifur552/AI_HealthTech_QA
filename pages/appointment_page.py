# pages/appointment_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.facility_dropdown = (By.ID, "combo_facility")
        self.visit_date_input = (By.ID, "txt_visit_date")
        self.comment_input = (By.ID, "txt_comment")
        self.book_button = (By.ID, "btn-book-appointment")
        self.confirmation_header = (By.TAG_NAME, "h2")

    def book_appointment(self, facility, date, comment):
        # হসপিটাল সিলেক্ট করা
        select = Select(self.driver.find_element(*self.facility_dropdown))
        select.select_by_visible_text(facility)
        
        # তারিখ বসানো
        date_box = self.driver.find_element(*self.visit_date_input)
        date_box.send_keys(date)
        
        # ম্যাজিক ট্রিক: ক্যালেন্ডার পপ-আপ সরাতে কীবোর্ডের ESCAPE বাটন চাপা!
        date_box.send_keys(Keys.ESCAPE)
        time.sleep(1)
        
        # কমেন্ট দেওয়া ও বুকিং বাটনে ক্লিক করা
        self.driver.find_element(*self.comment_input).send_keys(comment)
        self.driver.find_element(*self.book_button).click()
        
    def get_confirmation_text(self):
        return self.driver.find_element(*self.confirmation_header).text