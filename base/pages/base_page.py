from base.logger import BaseLogger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(BaseLogger):
    def __init__(self, driver, target_url: str):
        super().__init__()
        self.page = driver
        self.target_url = target_url

    def _get_wait(self, timeout: int = 10):
        self.debug(f'Get wait obj with timeout {timeout}')
        return WebDriverWait(self.page, timeout)

    def _locator_by_id(self, item_id: str) -> tuple[str, str]:
        self.debug(f'Get by id {item_id}')
        return (By.ID, item_id)

    def open(self):
        self.info(f'Open {self.target_url}')
        self.page.get(self.target_url)

    def get_by_id(self, item_id: str):
        locator = self._locator_by_id(item_id)
        return self.page.find_element(*locator)

    def wait_by_id(self, item_id: str):
        locator = self._locator_by_id(item_id)
        return self._get_wait().until(EC.element_to_be_clickable(locator))

    def get_by_data_qa_id(self, data_qa_id: str):
        self.debug(f'Get by data_qa_id: {data_qa_id}')
        return self.page.find_element(
            By.XPATH, f"//*[@data-qa-id='{data_qa_id}']"
        )
