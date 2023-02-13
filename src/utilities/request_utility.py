import requests
from src.utilities.credential_utility import CredentialsUtility
import logging as logger
import json
from src.configs.hosts_config import API_HOSTS
import pdb


class RequestUtility(object):
    def __init__(self):
        self.trello_creds = CredentialsUtility.get_trello_api_keys()
        self.base_url = API_HOSTS["test"]

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Bad status code. ' \
        f'"Expected {self.expected_status_code}. Actual status code: {self.status_code}.'\
        f'URL: {self.url}. Response: {self.rs_json}'


    def post(self, endpoint, params={}, headers=None, expected_status_code=200):
        self.url = self.base_url + endpoint + "/"
        self.payload = params | self.trello_creds

        if not headers:
            headers = {'Content-Type': 'application/json'}

        rs_api = requests.post(url=self.url, params=self.payload)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code

        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f'API Post response: {self.rs_json}')
        # pdb.set_trace()

        return rs_api.json()

    def get(self, endpoint, params={}, headers=None, expected_status_code=200):
        self.url = self.base_url + endpoint + "/"
        self.payload = params | self.trello_creds

        if not headers:
            headers = {"Accept": "application/json"}

        rs_api = requests.get(url=self.url, headers=headers, params=self.payload)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code

        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f'API Post response: {self.rs_json}')

        return rs_api.json()

    def delete(self, endpoint, params={}, headers=None, expected_status_code=200):
        self.url = self.base_url + endpoint + "/"
        self.payload = params | self.trello_creds

        if not headers:
            headers = {"Accept": "application/json"}

        rs_api = requests.delete(url=self.url, headers=headers, params=self.payload)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code

        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f'API Post response: {self.rs_json}')

        return rs_api.json()
    
    def put(self, endpoint, params={}, headers=None, expected_status_code=200):
        self.url = self.base_url + endpoint + "/"
        self.payload = params | self.trello_creds

        if not headers:
            headers = {'Content-Type': 'application/json'}

        rs_api = requests.put(url=self.url, params=self.payload)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        # pdb.set_trace()


        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f'API Post response: {self.rs_json}')
        # pdb.set_trace()

        return rs_api.json()