from .base_page import BasePage
from .user_home_page import UserHomePage

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

    def click_continue_button(self):
        element = self.get_by_xpath("//button[text()='Continue']", 0)
        element.click()

    def get_user_home_page(self):
        return UserHomePage(self.page)

    def get_invalid_email_error_message(self):
        element = self.get_by_id("error-cs-email-invalid")
        return element.text

    def get_required_username_error_message(self):
        element = self.get_by_id("error-cs-username-required")
        return element.text
