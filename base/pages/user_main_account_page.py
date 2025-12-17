from .base_page import BasePage

class UserMainAccPage(BasePage):
    def is_page_loaded(self):
        return self.get_by_id('explore-header').is_displayed()
