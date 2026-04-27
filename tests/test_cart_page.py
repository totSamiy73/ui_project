def test_empty_cart(cart):
    cart.open_page()
    cart.check_header_title("Order overview")
    cart.check_alert_message_empty_cart("Your cart is empty!")


def test_no_empty_cart(cart):
    name_product = cart.add_to_cart()
    cart.check_product_in_cart(name_product)
    cart.check_block_total_summ_product_in_cart()
    cart.check_block_total_summ_fields()


def test_cart_invalid_discount_code(cart):
    cart.add_to_cart()
    cart.check_alert_input_invalid_discount_code("qwerty")
