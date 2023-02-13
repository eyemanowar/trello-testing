import pdb
import os
import json
import pickle
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.browser_helpers.locator_helper import Locator
from selenium.webdriver.common.by import By
from src.utilities.credential_utility import CredentialsUtility



class BasePage(object):

    url = None

    def __init__(self, driver):
        self.trello_creds = CredentialsUtility.get_trello_creds()
        self.driver = driver
        self.cur_fil_dir = os.path.dirname(os.path.relpath(__file__))
        # pdb.set_trace()


    def get_cookies(self):
        return self.driver.get_cookies()

    def login(self, url):

        self.driver.get('https://trello.com/login')

        login_input = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(locator=Locator(by=By.CSS_SELECTOR,
            value="input#user")))
        login_input.send_keys(self.trello_creds['login'])

        login_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(mark=Locator(by=By.CSS_SELECTOR,
            value="input#login")))
        login_button.click()

        password_input = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(locator=Locator(by=By.CSS_SELECTOR,
            value="input#password")))
        password_input.send_keys(self.trello_creds['password'])

        pass_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(mark=Locator(by=By.CSS_SELECTOR,
            value="button#login-submit")))
        pass_button.click()

        self.driver.get(url)

    def dump_cookies(self):
        cookie_list = self.get_cookies()
        # pdb.set_trace()
        cookie_template = os.path.join(self.cur_fil_dir, '..', '..', 'data', 'cookies_dump.json')
        with open(cookie_template, 'w') as f:
            json.dump(cookie_list, f)

    def add_cookie(self):
        cookie_template = os.path.join(self.cur_fil_dir, '..', '..', 'data', 'cookies_dump.json')
        with open(cookie_template) as f:
            cookies = json.load(f)
        # cookies = pickle.load(open(cookie_template, "rb"))
        for cookie in cookies:
            if cookie['domain']:
                cookie['domain'] = ''
            self.driver.add_cookie(cookie)

    def go(self, url=url):
        self.driver.get(url)
        self.add_cookie()
        self.driver.get(url)
        try:
            login_element = WebDriverWait(self.driver, 5).until(
                    ec.visibility_of_element_located(locator=Locator(by=By.CSS_SELECTOR,value="button[data-testid='request-access-signup-button']"))
                )
            self.login(url=url)
            trello_element = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(mark=Locator(by=By.CSS_SELECTOR,value=f"span[title={'your account here'}]"))
            )
            self.dump_cookies()
        except:
            current_url = self.driver.current_url
            # pdb.set_trace()