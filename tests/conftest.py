from pytest import fixture
from selenium import webdriver

@fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    return driver
