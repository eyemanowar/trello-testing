from selenium.webdriver.common.by import By
from src.browser_helpers.base_element import BaseElement
from src.browser_helpers.base_page import BasePage
from src.browser_helpers.locator_helper import Locator



class NotFoundPage(BasePage):

    @property
    def not_found_h1(self):
        locator = Locator(by=By.CSS_SELECTOR, value="div[class='xx2hfsYaEqyPNz oZ0opQCkBo1dLq'] > h1")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )
