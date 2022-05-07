from enum import Enum
from tests.api.search_params import SearchParams
import pytest
import requests

URL = "https://demo.nopcommerce.com/product/search?"


class OrderBy(Enum):
    default = 0
    a_to_z = 5
    z_to_a = 6
    price_low_to_high = 10
    price_high_to_low = 11
    created_on = 15


class TestSearch:
    @staticmethod
    @pytest.mark.parametrize(
        "query, order_by, expected",
        [
            pytest.param("laptop", OrderBy.a_to_z, 5)
        ]
    )
    def test_order_by(query: str, order_by: OrderBy, expected: int):
        response = requests.get(URL + SearchParams(q=query, orderby=order_by.value).to_str())
        assert response.text.count("item-box") == expected
