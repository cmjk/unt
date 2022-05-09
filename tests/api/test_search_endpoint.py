import pytest
import requests
from assertpy import assert_that

from framework.common.product_item import ProductItem, Products
from framework.common.search_options import OrderBy
from framework.utils import read_config
from tests.api.search_params import SearchParams


class TestSearch:
    URL = read_config()['Constants']['SEARCH_URL']

    @staticmethod
    @pytest.mark.parametrize(
        "query",
        [
            pytest.param("laptop")
        ]
    )
    @pytest.mark.parametrize(
        "order_by, expected",
        [
            pytest.param(OrderBy.a_to_z, [Products.asus_n551,
                                          Products.hp_envy,
                                          Products.hp_spectre,
                                          Products.lenovo_thinkpad,
                                          Products.samsung_series9], id="A to Z"),
            pytest.param(OrderBy.z_to_a, [Products.samsung_series9,
                                          Products.lenovo_thinkpad,
                                          Products.hp_spectre,
                                          Products.hp_envy,
                                          Products.asus_n551], id="Z to A"),
            pytest.param(OrderBy.price_low_to_high, [Products.hp_spectre,
                                                     Products.lenovo_thinkpad,
                                                     Products.hp_envy,
                                                     Products.asus_n551,
                                                     Products.samsung_series9], id="Low to High"),
            pytest.param(OrderBy.price_high_to_low, [Products.samsung_series9,
                                                     Products.asus_n551,
                                                     Products.hp_envy,
                                                     Products.lenovo_thinkpad,
                                                     Products.hp_spectre], id="High to Low"),

        ]
    )
    def test_order_by(query: str, order_by: OrderBy, expected: list[ProductItem]):
        response = requests.get(TestSearch.URL + SearchParams(q=query, orderby=order_by.value).to_str())
        assert_that(ProductItem.from_html(response.text)).is_equal_to(expected)

    @staticmethod
    @pytest.mark.parametrize(
        "query",
        [
            pytest.param("laptop")
        ]
    )
    @pytest.mark.parametrize(
        "display_per_page, expected",
        [
            pytest.param(3, [Products.asus_n551,
                             Products.samsung_series9,
                             Products.hp_spectre], id="Display 3 per page"),
            pytest.param(6, [Products.asus_n551,
                             Products.samsung_series9,
                             Products.hp_spectre,
                             Products.hp_envy,
                             Products.lenovo_thinkpad], id="Display 6 per page")
        ])
    def test_display_per_page(query: str, display_per_page: int, expected: list[ProductItem]):
        response = requests.get(TestSearch.URL + SearchParams(q=query, pagesize=display_per_page).to_str())
        assert_that(ProductItem.from_html(response.text)).is_equal_to(expected)
