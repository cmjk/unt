from framework.utils import read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver


class Actions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = read_config()["Constants"]["TIMEOUT_s"]

    def is_element_visible(self, locator: tuple) -> bool:
        wait = WebDriverWait(self.driver, self.timeout)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
