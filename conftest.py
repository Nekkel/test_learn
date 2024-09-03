import pytest
from selenium import webdriver
from pages.shop_page import HomePage, BasePage

@pytest.fixture(scope="function")
def setup_selenium():
    # global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
