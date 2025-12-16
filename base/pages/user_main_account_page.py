from .base_page import BasePage

class UserMainAccPage(BasePage):
    def wait_home_page(self):
        element = self.get_by_id('explore-header')
        if not element.is_displayed():
            raise AssertionError('Home page not found')