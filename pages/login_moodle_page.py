from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginMoodlePage(BasePage):
    USER_EMAIL = (By.ID, 'username')
    USER_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'loginbtn')

    def login(self, username, password):
        self.enter_text(self.USER_EMAIL, username)
        self.enter_text(self.USER_PASSWORD, password)
        self.click(self.LOGIN_BTN)

    