import os

class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_trello_api_keys():

        trello_key = os.environ.get('TRELLO_KEY')
        trello_token = os.environ.get('TRELLO_TOKEN')
        org_id = os.environ.get('ORG_ID')

        if not trello_key or not trello_token:
            raise Exception('The Api credntials TRELLO_KEY and TRELLO_TOKEN must be in the env variable')
        else:
            return {'key': trello_key, 'token': trello_token, 'org_id': org_id}

    @staticmethod
    def get_trello_creds():

        trello_login = os.environ.get('TRELLO_LOGIN')
        trello_password = os.environ.get('TRELLO_PASSWORD')

        if not trello_login or not trello_password:
            raise Exception('The Api credntials TRELLO_LOGIN and TRELLO_PASSWORD must be in the env variable')
        else:
            return {'login': trello_login, 'password': trello_password}