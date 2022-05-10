import pytest
from assertpy import assert_that

import framework.elements as elements
from framework.actions import Actions
from framework.common.product_item import ProductItem, Products
from framework.common.search_options import OrderBy
from framework.utils import read_config


class TestSearch:
    no_products_found = "No products were found that matched your criteria."

    @staticmethod
    def test_search_is_present_on_page(actions: Actions):
        assert actions.is_element_visible(elements.SEARCH_BUTTON)
        assert actions.is_element_visible(elements.SEARCH_INPUT)

    @staticmethod
    @pytest.mark.parametrize(
        "search_query, count",
        [
            pytest.param("gift card", 3, id="Some results"),
            pytest.param("camera", 1, id="One result"),
            pytest.param("longstring", 0, id="No results")
        ]
    )
    def test_search_results(search: pytest.fixture, actions: Actions, search_query: str, count: int):
        """
        Tests search results for different input queries
        """
        assert count == actions.get_element_count(elements.PRODUCT)
        if count == 0:
            assert_that(TestSearch.no_products_found).is_equal_to(actions.get_element_text(elements.NO_RESULTS))

    @staticmethod
    @pytest.mark.parametrize(
        "search_query",
        [
            pytest.param("_", id="Minimum search term length is 1 symbol")
        ]
    )
    def test_search_valid_term_length(search: pytest.fixture, actions: Actions, search_query: str):
        """
        Tests minimum valid search term
        """
        assert_that(TestSearch.no_products_found).is_equal_to(actions.get_element_text(elements.NO_RESULTS))

    @staticmethod
    @pytest.mark.parametrize(
        "search_query, order_by, expected",
        [
            pytest.param("laptop", OrderBy.price_low_to_high, [Products.lenovo_thinkpad,
                                                               Products.asus_n551])
        ]
    )
    def test_sort_by(search: pytest.fixture, actions: Actions, search_query: str, order_by: OrderBy,
                     expected: list[ProductItem]):
        """
        Tests that sort by dropdown option is applied
        """
        actions.select_dropdown_value(elements.SORT_BY, str(order_by.value), loading_locator=elements.SEARCH_LOADING)
        assert_that(ProductItem.from_html(actions.driver.page_source)).is_equal_to(expected)

    @staticmethod
    @pytest.mark.parametrize(
        "search_query, link_to_product",
        [
            pytest.param("asus", f"{read_config()['Constants']['DEMO_URL']}asus-n551jk-xo076h-laptop")
        ]
    )
    @pytest.mark.parametrize(
        "locator",
        [
            pytest.param(elements.PRODUCT_NAME, id="Product Name"),
            pytest.param(elements.PRODUCT_IMAGE, id="Product Image")
        ]
    )
    def test_redirect_to_product_page(search: pytest.fixture, actions: Actions, search_query: str, locator: tuple,
                                      link_to_product: str):
        """
        Tests that clicking the product name or the product image takes user to the product page
        TODO: verify home page
        """
        assert_that(actions.get_href_value(locator)).is_equal_to(link_to_product)
