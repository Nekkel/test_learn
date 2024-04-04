class WebLocators:

    top_menu_catalog_btn = '//*[@id="main-nav"]//li[2]/a'


    catalog_menu_btn_template = f'//ul[@class="categories"]//a[contains(text(), "%s")]'
    catalog_prod_card_template = f'//div[@class="product-card-info"]/a[contains(text(), "%s")]'


    prod_page_preorder_btn = '//button[contains(@class, "tocart-button")]'
    prod_page_to_cart_btn = '//div[@class="modal-footer"]/button]'


    # Cart page
    cart_pay_btn = '//a[@data-onClick="createOrder"]'
    cart_email_error_msg = '//div[contains(text(), "Некорректный адрес электронной почты!")]'



