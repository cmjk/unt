import pytest

from framework.elements import SEARCH_BUTTON, SEARCH_INPUT, PRODUCT, NO_RESULTS, WARNING
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
            pytest.param("gift card", 3),
            pytest.param("camera", 1),
            pytest.param("longstring", 0)
        ]
    )
    def test_search_results(actions: Actions, search_query: str, count: int):
        actions.input_text(SEARCH_INPUT, search_query)
        actions.click(SEARCH_BUTTON)
        assert count == actions.get_element_count(PRODUCT)
        if count == 0:
            assert TestSearch.no_products_found == actions.get_element_text(NO_RESULTS)

    @staticmethod
    @pytest.mark.parametrize(
        "search_query",
        [
            pytest.param("_"),
            pytest.param("__"),
        ]
    )
    def test_search_invalid_term_length(actions: Actions, search_query: str):
        actions.input_text(SEARCH_INPUT, search_query)
        actions.click(SEARCH_BUTTON)
        assert "Search term minimum length is 3 characters" == actions.get_element_text(WARNING)

    @staticmethod
    @pytest.mark.parametrize(
        "search_query",
        [
            pytest.param("___"),
        ]
    )
    def test_search_valid_term_length(actions: Actions, search_query: str):
        actions.input_text(SEARCH_INPUT, search_query)
        actions.click(SEARCH_BUTTON)
        assert TestSearch.no_products_found == actions.get_element_text(NO_RESULTS)
