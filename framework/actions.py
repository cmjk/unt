from framework.utils import read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class Actions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = read_config()["Constants"]["TIMEOUT_s"]

    def _find_element(self, locator: tuple) -> WebElement:
        try:
            return WebDriverWait(self.driver, self.timeout).\
                until(ec.visibility_of_element_located(locator))
        except TimeoutException as e:
            raise TimeoutException(f"Element with locator {locator} was not found in time.") from e

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

    def get_element_text(self, locator: tuple) -> str:
        return self._find_element(locator).text

    def select_dropdown_value(self, locator: tuple, value: str, loading_locator: tuple = None):
        dropdown = Select(self._find_element(locator))
        dropdown.select_by_value(value)
        if loading_locator:
            self.wait_for_element_to_not_be_visible(loading_locator)

    def wait_for_element_to_not_be_visible(self, locator: tuple):
        WebDriverWait(self.driver, self.timeout, poll_frequency=0.2). \
            until(ec.invisibility_of_element_located(locator))

    def get_href_value(self, locator: tuple) -> str:
        return self._find_element(locator).get_attribute("href")
