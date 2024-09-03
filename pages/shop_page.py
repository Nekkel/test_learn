from locators.locators import WebLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.color import Color

import webcolors
import re
from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_xpath_element(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_css_element(self, css):
        return self.driver.find_element(By.CSS_SELECTOR, css)

    def wait_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        return element

    def find_and_click(self, xpath):
        self.wait_element(xpath).click()

    # def click(self, xpath):
    #     element = self.driver.find_element(By.XPATH, xpath)
    #     element.click()

    def check_color(self, element, exp_color):
        e_color = element.value_of_css_property("color")
        e_color = re.findall(r'\d+', e_color)
        e_color_hex = webcolors.rgb_to_hex((int(e_color[0]), int(e_color[1]), int(e_color[2])))
        assert e_color_hex == exp_color


class HomePage(BasePage):

    def home_click_catalog(self):
        self.find_and_click(WebLocators.top_menu_catalog_btn)


class CatalogPage(BasePage):

    def catalog_click_menu_btn(self, menu_btn_name):
        locator = (WebLocators.catalog_menu_btn_template % menu_btn_name)
        self.find_and_click(locator)

    def catalog_click_product_card(self, text):
        locator = (WebLocators.catalog_prod_card_template % text)
        self.find_and_click(locator)


class ProductPage(BasePage):

    def prod_click_preorder(self):
        self.find_and_click(WebLocators.prod_page_preorder_btn)

    def prod_click_to_cart(self):
        self.find_and_click(WebLocators.prod_page_to_cart_btn)


class CartPage(BasePage):

    def cart_click_pay_btn(self):
        self.find_and_click(WebLocators.cart_pay_btn)

    def cart_check_email_error_color(self, color):
        e = self.find_xpath_element(WebLocators.cart_email_error_msg)
        self.check_color(e, color)
