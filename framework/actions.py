from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from framework.utils import read_config


class Actions:
    """
    Common WebDriver actions
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = read_config()["Constants"]["TIMEOUT_s"]

    def _find_element(self, locator: tuple) -> WebElement:
        """
        Waits for an element to be visible and returns it
        If not found within timeout, raises TimeoutException
        """
        try:
            return WebDriverWait(self.driver, self.timeout). \
                until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} was not found in time.") from None

    def is_element_visible(self, locator: tuple) -> bool:
        """
        Checks whether an element is visible or not
        """
        try:
            self._find_element(locator)
            return True
        except TimeoutException:
            return False

    def input_text(self, locator: tuple, text: str):
        """
        Clears an input field and writes text to it
        """
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator: tuple):
        """
        Wait for an element to appear and clicks it
        """
        self._find_element(locator).click()

    def get_element_count(self, locator: tuple) -> int:
        """
        Gets the count of elements matching a locator
        """
        try:
            self._find_element(locator)
        except TimeoutException:
            return 0
        return len(self.driver.find_elements(*locator))

    def get_element_text(self, locator: tuple) -> str:
        """
        Gets text from an element
        """
        return self._find_element(locator).text

    def select_dropdown_value(self, locator: tuple, value: str, loading_locator: tuple = None):
        """
        Selects dropdown option by value
        If loading_locator is specified, waits for it to stop being visible
        """
        dropdown = Select(self._find_element(locator))
        dropdown.select_by_value(value)
        if loading_locator:
            self.wait_for_element_to_not_be_visible(loading_locator)

    def wait_for_element_to_not_be_visible(self, locator: tuple):
        """
        Waits for an element to stop being visible
        """
        WebDriverWait(self.driver, self.timeout, poll_frequency=0.2). \
            until(ec.invisibility_of_element_located(locator))

    def get_href_value(self, locator: tuple) -> str:
        """
        Gets href attribute value from an element
        """
        return self._find_element(locator).get_attribute("href")
