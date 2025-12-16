from .base_page import BasePage

class MainPage(BasePage):
    def close_cookie(self):
        element = self.get_by_id('onetrust-close-btn-container')
        element.click()

    def click_login(self):
        element = self.get_by_data_qa_id('login-select')
        element.click()

    def click_hudl_login(self):
        element = self.get_by_data_qa_id('login-hudl')
        element.click()

    def set_email_input(self, email):
        element = self.get_by_xpath("//input[@id='username']")
        element.send_keys(email)

    def set_password_input(self, password):
        element = self.get_by_xpath("//input[@id='password']")
        element.send_keys(password)

    def click_login2(self):
        element = self.get_by_xpath("//button[text()='Continue']", 0)
        element.click()

    def wait_home_page(self):
        element = self.get_by_id('explore-header')
        if not element.is_displayed():
            raise AssertionError('Home page not found')

