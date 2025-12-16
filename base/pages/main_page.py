from .base_page import BasePage

class MainPage(BasePage):
    def close_cookie(self):
        element = self.wait_by_id('onetrust-close-btn-container')
        element.click()

    def click_login(self):
        element = self.get_by_data_qa_id('login-select')
        element.click()

    def click_hudl_login(self):
        element = self.get_by_data_qa_id('login-hudl')
        element.click()
