from selenium.webdriver.common.by import By


SEARCH_INPUT = By.CSS_SELECTOR, "#small-search-box-form > input"
SEARCH_BUTTON = By.CSS_SELECTOR, "#small-search-box-form > button[type='submit']"
PRODUCT = By.CLASS_NAME, "product-item"
NO_RESULTS = By.CLASS_NAME, "no-result"
WARNING = By.CLASS_NAME, "warning"
