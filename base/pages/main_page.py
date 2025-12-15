from .base_page import BasePage

class MainPage(BasePage):
    ...
    def close_cookie(self):
        element = self.get_by_id('onetrust-close-btn-container')
        element.click()
