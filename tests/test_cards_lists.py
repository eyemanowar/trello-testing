import pytest
import pdb
from src.utilities.generic_utilities import generate_custom_string
from src.utilities.request_utility import RequestUtility
from src.api_helpers.board_helper import BoardHelper
from src.api_helpers.card_helper import CardHelper
from src.page_helpers.list_page import ListPage
from src.page_helpers.card_page import CardPage
from src.page_helpers.board_not_found_page import NotFoundPage

@pytest.mark.tcid4
def test_create_list(driver):
    board_helper = BoardHelper()
    board = board_helper.get_random_board()
    rs_helper = RequestUtility()

    payload = {'name': generate_custom_string()}
    endpoint = f"boards/{board['id']}/lists"
    rs_api = rs_helper.post(endpoint=endpoint, params=payload)
    assert rs_api['name'] == payload['name'], f"The created list has the wrong name" \
                                              f"Expected: {payload['name']}. Actual: {rs_api['name']}"

    page = ListPage(driver)
    url = board['url']
    page.go(url=url)
    lists_on_page = page.list_names()

    assert payload['name'] in lists_on_page, f"Board do not include given list name" \
                                             f"Expected: {payload['name']}. Actual names: {lists_on_page}"


@pytest.mark.tcid5
def test_create_card(driver):
    # make an api call
    board_helper = BoardHelper()
    rand_list = board_helper.get_random_list()

    rs_helper = RequestUtility()

    payload = {
        'name': generate_custom_string(),
        'idList': rand_list['id']
    }
    rs_api = rs_helper.post(endpoint="cards", params=payload)

    assert rs_api['name'] == payload['name'], f"The created board has the wrong name" \
                                              f"Expected: {payload['name']}. Actual: {rs_api['name']}"

    page = CardPage(driver)
    url = rs_api['url']
    page.go(url=url)

    assert page.card_name == payload['name'], f"The created board has the wrong name on the live site" \
                                              f"Expected: {payload['name']}. Actual: {page.card_name}"


@pytest.mark.tcid6
def test_delete_card(driver):

    card_helper = CardHelper()
    card = card_helper.get_random_card()

    endpoint = f"cards/{card['id']}"

    rs_helper = RequestUtility()
    rs_api = rs_helper.delete(endpoint=endpoint)

    page = NotFoundPage(driver)
    url = card['url']
    page.go(url=url)

    assert page.not_found_h1.text == 'Card not found.'
    

@pytest.mark.tcid7
def test_update_a_list_on_board(driver):
    
    board_helper = BoardHelper()
    rand_list = board_helper.get_random_list()
    
    rs_helper = RequestUtility()
    endpoint = f"lists/{rand_list['id']}"
    payload = {
        'name': "new name: " + generate_custom_string(),
    }
    # pdb.set_trace()
    rs_api = rs_helper.put(endpoint=endpoint, params=payload)
    
    page = ListPage(driver)
    url = "https://trello.com/b/j61Mh93S/" + rand_list["idBoard"]
    page.go(url=url)
    lists_on_page = page.list_names()
    
    assert payload['name'] in lists_on_page, f'''The updated list name {payload["name"]} is not found on the board [link: {url}].
                                                The actual list of boards is following: {lists_on_page}'''




