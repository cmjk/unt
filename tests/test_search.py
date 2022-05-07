from framework.elements import SEARCH_BUTTON, SEARCH_INPUT
from framework.actions import Actions


class TestSearch:
    @staticmethod
    def test_search_is_present_on_page(actions: Actions):
        assert actions.is_element_visible(SEARCH_BUTTON)
        assert actions.is_element_visible(SEARCH_INPUT)
