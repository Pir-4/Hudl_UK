from .base_page import BasePage
from .user_main_account_page import UserMainAccPage

class LogInPage(BasePage):
    def set_email_input(self, email):
        element = self.get_by_xpath("//input[@id='username']")
        element.send_keys(email)

    def set_password_input(self, password):
        element = self.get_by_xpath("//input[@id='password']")
        element.send_keys(password)

    def click_login2(self):
        element = self.get_by_xpath("//button[text()='Continue']", 0)
        element.click()

    def get_user_main_acc_page(self):
        return UserMainAccPage(self.page)