from framework.utils import read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Actions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = read_config()["Constants"]["TIMEOUT_s"]

    def _find_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).\
            until(ec.visibility_of_element_located(locator))

    def is_element_visible(self, locator: tuple) -> bool:
        try:
            self._find_element(locator)
            return True
        except TimeoutException:
            return False

    def input_text(self, locator: tuple, text: str):
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator: tuple):
        self._find_element(locator).click()

    def get_element_count(self, locator: tuple) -> int:
        try:
            self._find_element(locator)
        except TimeoutException:
            return 0
        return len(self.driver.find_elements(*locator))

    def get_element_text(self, locator) -> str:
        return self._find_element(locator).text
