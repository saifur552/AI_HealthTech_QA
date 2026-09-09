# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
        
        # Locators (adress of the components of site's)
        self.username_input = (By.ID, "txt-username")
        self.password_input = (By.ID, "txt-password")
        self.login_button = (By.ID, "btn-login")

    def load(self):
        """funtion for opening logic page"""
        self.driver.get(self.url)

    def login(self, username, password):
        """login via userid and pass"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()