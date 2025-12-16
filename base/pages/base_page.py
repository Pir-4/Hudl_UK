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
        if not timeout:
            self.debug(f'Get wait obj with timeout {timeout}')
        return WebDriverWait(self.page, timeout)

    def _locator_by_id(self, item_id: str) -> tuple[str, str]:
        self.debug(f'Get by id {item_id}')
        return (By.ID, item_id)

    def _locator_by_xpath(self, xpath: str) -> tuple[str, str]:
        self.debug(f'Get by xpath {xpath}')
        return (By.XPATH, xpath)

    @property
    def title(self):
        return self.page.title

    def open(self):
        self.info(f'Open {self.target_url}')
        self.page.get(self.target_url)
        t = self.page.title # 'Hudl • The leader in sports technology, video analysis & data'
        g = 5

    def get_by_id(self, item_id: str, timeout: int = 10):
        locator = self._locator_by_id(item_id)
        return self._get_wait(timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_by_xpath(self, xpath: str, timeout: int = 10):
        locator = self._locator_by_xpath(xpath)
        return self._get_wait(timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_by_data_qa_id(self, data_qa_id: str):
        self.debug(f'Get by data_qa_id: {data_qa_id}')
        locator = self._locator_by_xpath(f"//*[@data-qa-id='{data_qa_id}']")
        return self.page.find_element(*locator)
