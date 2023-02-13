from selenium.webdriver.common.by import By
from src.browser_helpers.base_element import BaseElement
from src.browser_helpers.base_page import BasePage
from src.browser_helpers.locator_helper import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class CardPage(BasePage):

    @property
    def card_name(self):
        locator = Locator(by=By.CSS_SELECTOR, value="h2#js-dialog-title")
        name = self.driver.find_element(by=locator[0], value=locator[1])
        return name.get_attribute("textContent")

        # return BaseElement(
        #     driver=self.driver,
        #     by=locator[0],
        #     value=locator[1]
        # )