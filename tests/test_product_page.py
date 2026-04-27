def test_details_product(product):
    product.open_page()
    product.check_title_product("Office Design Software")
    product.check_currency_value()
    product.check_field_count_and_add()


def test_add_cart_product(product):
    product.open_page()
    product.add_to_cart()
    product.check_product_in_cart()


def test_field_search(product):
    product.open_page()
    product.field_search("qwerty")
    product.check_no_results_after_search("qwerty")
