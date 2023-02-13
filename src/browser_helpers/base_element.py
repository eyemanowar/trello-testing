from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseElement(object):

    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self, string):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator=self.locator))
        element.send_keys(string)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(mark=self.web_element))
        element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    @property
    def inner_text(self):
        text = self.web_element.get_attribute("innerText")
        return text

    @property
    def hidden_text(self):
        text = self.web_element.get_attribute("textContent")
        return text
