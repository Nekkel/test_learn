from pages.shop_page import HomePage, CatalogPage, ProductPage, CartPage
from time import sleep


class TestFirstClass:
    def test_first(self, setup_selenium):
        driver = setup_selenium
        home = HomePage(driver)
        catalog = CatalogPage(driver)
        prod_card = ProductPage(driver)
        cart = CartPage(driver)

        driver.get("https://shop.bbrfactory.com/")

        home.home_click_catalog()
        catalog.catalog_click_menu_btn('Сумки и рюкзаки')
        catalog.catalog_click_product_card('Джим Вернулся К7')
        # prod_card.prod_click_preorder()
        # cart.cart_click_pay_btn()
        cart.cart_check_email_error_color('#ff0000')
