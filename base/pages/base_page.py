from base.logger import BaseLogger
from selenium.webdriver.common.by import By


class BasePage(BaseLogger):
    def __init__(self, driver, target_url: str):
        super().__init__()
        self.page = driver
        self.target_url = target_url


    def open(self):
        self.info(f'Open {self.target_url}')
        self.page.get(self.target_url)


    def get_by_id(self, item_id):
        self.debug(f'Get by id {item_id}')
        return self.page.find_element(By.ID, item_id)

    def get_by_data_qa_id(self, data_qa_id: str):
        self.debug(f'Get by data_qa_id: {data_qa_id}')
        return self.page.find_element(
            By.XPATH, f"//*[@data-qa-id='{data_qa_id}']"
        )
