from .base_page import BasePage
from .user_main_account_page import UserMainAccPage

class LogInPage(BasePage):
    @property
    def get_email_input(self):
        return self.get_by_xpath("//input[@id='username']")

    @property
    def get_password_input(self):
        return self.get_by_xpath("//input[@id='password']")

    def set_email_input(self, email):
        self.get_email_input.send_keys(email)

    def set_password_input(self, password):
        self.get_password_input.send_keys(password)

    def is_email_input_displayed(self):
        return self.get_email_input.is_displayed()

    def is_password_input_displayed(self):
        return self.get_password_input.is_displayed()

    def click_login2(self):
        element = self.get_by_xpath("//button[text()='Continue']", 0)
        element.click()

    def get_user_main_acc_page(self):
        return UserMainAccPage(self.page)