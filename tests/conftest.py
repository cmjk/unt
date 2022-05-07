import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from framework.utils import read_config
from framework.actions import Actions
from selenium.webdriver.common.by import By


@pytest.fixture(name="driver", scope="function")
def start_webdriver() -> WebDriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(read_config()["Constants"]["URL"])
    frame = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(frame)
    yield driver
    driver.quit()


@pytest.fixture(name="actions", scope="function")
def fixture_actions(driver: WebDriver):
    yield Actions(driver=driver)
