from selenium.webdriver.common.by import By


class LocatorsCart:
    HEADER_TITLE = (By.CLASS_NAME, "mb-4")
    ALERT_MESSAGE = (By.CLASS_NAME, "js_cart_lines")
    PRODUCTS_TITLE = (By.CLASS_NAME, 'o_wsale_products_item_title')
    BUTTON_ADD = (By.ID, "add_to_cart")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, ".btn.btn-secondary")
    QUANTITY_IN_CART = (By.CSS_SELECTOR, '.my_cart_quantity')
    BUTTON_CART = (By.CSS_SELECTOR, ".fa.fa-shopping-cart.fa-stack")
    TITLE_PRODUCT_IN_CART = (By.CLASS_NAME, "d-inline")
    BLOCK_SUMM = (By.CLASS_NAME, "card-body")
    SUBTOTAL = (By.ID, "cart_total_subtotal")
    DISCOUNT_FIELD = (By.XPATH, '//input[@class="form-control"]')
    BUTTON_APPLY = (By.XPATH, '//a[text()="Apply"]')
    ALERT_NO_DISCOUNT = (By.XPATH, '//div[@role="alert"]')


class LocatorsCategory:
    FIELDS_SEARCH = (By.XPATH, '//input[@type="search"]')
    BUTTON_GLASS = (By.CSS_SELECTOR, ".btn.oe_search_button.btn.btn-light")
    PRODUCTS_TITLE = (By.CLASS_NAME, 'o_wsale_products_item_title')
    MESS_NO_RESULT = (By.CLASS_NAME, "mt8")
    MESS_NO_RESULT_UNDER = (By.XPATH, '//*[contains(text(), "No results for")]')
    PRICE_RANGE = (By.CLASS_NAME, 'multirange-wrapper')
    CHECKBOX_ALUM = (By.ID, "1-2")
    PRODUCT_IMAGES = (By.CLASS_NAME, 'oe_product_image')
    SWITCHER_PRICELIST = (By.XPATH, '//a[@data-bs-toggle="dropdown" and @role="button"]')
    SWITCHER_EUR = (By.XPATH, '//span[text()="EUR"]')
    PRODUCT_PRICE = (By.CLASS_NAME, "product_price")


class LocatorsProduct:
    TITLE_PRODUCT = (By.TAG_NAME, "h1")
    CURRENCY_VALUE = (By.CLASS_NAME, "oe_currency_value")
    BUTTON_REMOVE = (By.XPATH, '//a[@title="Remove one"]')
    BUTTON_ADD = (By.XPATH, '//a[@title="Add one"]')
    FIELD_COUNT = (By.XPATH, '//input[@name="add_qty"]')
    BUTTON_ADD_CART = (By.ID, 'add_to_cart')
    QUANTITY_IN_CART = (By.CSS_SELECTOR, '.my_cart_quantity')
    BUTTON_CART = (By.CSS_SELECTOR, ".fa.fa-shopping-cart.fa-stack")
    TITLE_PRODUCT_IN_CART = (By.CLASS_NAME, "d-inline")
    FIELDS_SEARCH = (By.XPATH, '//input[@type="search"]')
    BUTTON_GLASS = (By.CSS_SELECTOR, ".btn.oe_search_button.btn.btn-light")
    MESS_NO_RESULT = (By.CLASS_NAME, "mt8")
    MESS_NO_RESULT_UNDER = (By.XPATH, '//*[contains(text(), "No results for")]')
