import pdb
import random
from src.api_helpers.board_helper import BoardHelper
from src.utilities.request_utility import RequestUtility

class CardHelper(object):

    def __init__(self):
        self.board_helper = BoardHelper()
        self.board = self.board_helper.get_random_board()
        self.rs_helper = RequestUtility()

    def get_random_card(self):

        url = f"boards/{self.board['id']}/cards"

        headers = {
            "Accept": "application/json"
        }

        rs_api = self.rs_helper.get(endpoint=url, headers=headers)
        while len(rs_api) == 0:
            rs_api = self.rs_helper.get(endpoint=url, headers=headers)

        return random.choice(rs_api)