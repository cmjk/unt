import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from framework.utils import read_config, run_headless
from framework.actions import Actions
from selenium.webdriver.common.by import By
from framework.elements import SEARCH_BUTTON, SEARCH_INPUT


def _get_chrome_options() -> webdriver.ChromeOptions:
    """
    Sets up all of the options for running tests in Chrome.
    :return: An instance of ChromeOptions.
    """
    chrome_options = webdriver.ChromeOptions()
    headless_mode = run_headless()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "intl.accept_languages": "en,en_US",
        },
    )
    chrome_options.add_argument("start-maximized")

    if headless_mode:
        chrome_options.headless = True
        chrome_options.page_load_strategy = "normal"

        chrome_options.add_argument("--disable-browser-side-navigation")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--dns-prefetch-disable")
        chrome_options.add_argument("--force-device-scale-factor=1")
        chrome_options.add_argument("--no-sandbox")

        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

    return chrome_options


@pytest.fixture(name="driver", scope="function")
def start_webdriver() -> WebDriver:
    driver = webdriver.Chrome(options=_get_chrome_options())
    driver.get(read_config()["Constants"]["URL"])
    frame = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(frame)
    yield driver
    driver.quit()


@pytest.fixture(name="actions", scope="function")
def fixture_actions(driver: WebDriver):
    yield Actions(driver=driver)


@pytest.fixture(name="search")
def fixture_search(actions: Actions, search_query: str):
    actions.input_text(SEARCH_INPUT, search_query)
    actions.click(SEARCH_BUTTON)
