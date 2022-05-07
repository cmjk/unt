import pytest

from framework.elements import SEARCH_BUTTON, SEARCH_INPUT, PRODUCT, NO_RESULTS
from framework.actions import Actions


class TestSearch:
    no_products_found = "No products were found that matched your criteria."

    @staticmethod
    def test_search_is_present_on_page(actions: Actions):
        assert actions.is_element_visible(SEARCH_BUTTON)
        assert actions.is_element_visible(SEARCH_INPUT)

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
        assert count == actions.get_element_count(PRODUCT)
        if count == 0:
            assert TestSearch.no_products_found == actions.get_element_text(NO_RESULTS)

    @staticmethod
    @pytest.mark.parametrize(
        "search_query",
        [
            pytest.param("_", id="Minimum search term length is 1 symbol"),
        ]
    )
    def test_search_valid_term_length(search: pytest.fixture, actions: Actions, search_query: str):
        assert TestSearch.no_products_found == actions.get_element_text(NO_RESULTS)
