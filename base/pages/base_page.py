from base.logger import BaseLogger


class BasePage(BaseLogger):
    def __init__(self, driver, target_url: str):
        super().__init__()
        self.page = driver
        self.target_url = target_url


    def open(self):
        self.info(f'Open {self.target_url}')
        self.page.get(self.target_url)
