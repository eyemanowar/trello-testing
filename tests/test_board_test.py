import pytest
import pdb
from src.utilities.generic_utilities import generate_custom_string
from src.utilities.request_utility import RequestUtility
from src.page_helpers.board_page import BoardPage
from src.api_helpers.board_helper import BoardHelper
from src.page_helpers.board_not_found_page import NotFoundPage


@pytest.mark.tcid1
@pytest.mark.board
def test_create_board(driver):
    # make an api call
    rs_helper = RequestUtility()
    payload = {'name': generate_custom_string()}
    rs_api = rs_helper.post(endpoint="boards", params=payload)
    # pdb.set_trace()

    # verify the call
    assert rs_api['name'] == payload['name'], f"The created board has the wrong name" \
                                              f"Expected: {payload['name']}. Actual: {rs_api['name']}"

    # connect to the trello via selenium
    board_page = BoardPage(driver)
    url = rs_api['shortUrl']
    # url = 'https://trello.com/b/j61Mh93S/vmoondkevs'
    board_page.go(url=url)
    assert board_page.board_name.text == rs_api['name'], f"Board page is not correct." \
                                        f"Expected name:{rs_api['name']}. Actual name:{board_page.board_name.text}."



@pytest.mark.tcid2
@pytest.mark.board
def test_get_board(driver):
    board_helper = BoardHelper()
    board = board_helper.get_random_board()

    rs_helper = RequestUtility()
    endpoint = f"boards/{board['id']}"
    rs_api = rs_helper.get(endpoint=endpoint)

    assert board['id'] == rs_api['id'], f'Get call returned incorrect board. Expected board id: {board["id"]}' \
                                     f'Actual board id: {rs_api["id"]}'

    board_name = rs_api['name']
    board_url = rs_api['url']

    board_page = BoardPage(driver)
    board_page.go(url=board_url)
    assert board_page.board_name.text == rs_api['name'], f"Board page is not correct." \
                                                f"Expected name:{board_name}. Actual name:{board_page.board_name.text}"

@pytest.mark.tcid3
@pytest.mark.board
def test_delete_board(driver):
    board_helper = BoardHelper()
    board = board_helper.get_random_board()

    rs_helper = RequestUtility()
    endpoint = f"boards/{board['id']}"
    board_url = board['url']

    rs_api = rs_helper.delete(endpoint=endpoint)

    board_page_not_found = NotFoundPage(driver)
    board_page_not_found.go(url=board_url)

    assert board_page_not_found.not_found_h1.text == 'Board not found.'
