import pdb

from selenium.webdriver.common.by import By
from src.browser_helpers.base_page import BasePage
from src.browser_helpers.locator_helper import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ListPage(BasePage):

    def list_names(self):
        locator = Locator(by=By.CSS_SELECTOR, value="h2[class='list-header-name-assist js-list-name-assist']")
        list_of_names = self.driver.find_elements(by=locator[0], value=locator[1] )
        return [name.get_attribute("textContent") for name in list_of_names]
