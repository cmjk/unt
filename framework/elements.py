from selenium.webdriver.common.by import By


SEARCH_INPUT = By.CSS_SELECTOR, "#small-search-box-form > input"
SEARCH_BUTTON = By.CSS_SELECTOR, "#small-search-box-form > button[type='submit']"
PRODUCT = By.CLASS_NAME, "product-item"
NO_RESULTS = By.CLASS_NAME, "no-result"
IFRAME = By.TAG_NAME, "iframe"
SORT_BY = By.CSS_SELECTOR, "select#products-orderby"
SEARCH_LOADING = By.CLASS_NAME, "ajax-products-busy"
PRODUCT_IMAGE = By.CSS_SELECTOR, ".picture > a"
PRODUCT_NAME = By.CSS_SELECTOR, ".product-title > a"
