import pdb
from src.utilities.request_utility import RequestUtility
from src.utilities.credential_utility import CredentialsUtility
import random


class BoardHelper(object):

    def __init__(self):
        self.cred = CredentialsUtility().get_trello_api_keys()
        self.org_id = self.cred['org_id']
        self.rs_helper = RequestUtility()

    def get_random_board(self):

        url = f"organizations/{self.org_id}/boards"

        headers = {
            "Accept": "application/json"
        }

        rs_api = self.rs_helper.get(endpoint=url, headers=headers)
        # pdb.set_trace()
        boards_list = []
        for board in rs_api:
            if not board['closed']:
                boards_list.append(board)
        return random.choice(boards_list)

    def get_random_list(self):

        self.board = self.get_random_board()

        url = f"boards/{self.board['id']}/lists"

        headers = {
            "Accept": "application/json"
        }

        rs_api = self.rs_helper.get(endpoint=url, headers=headers)
        return random.choice(rs_api)
