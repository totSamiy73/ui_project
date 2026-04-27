from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.locators_cart import LocatorsCart


class CartPage(BasePage):
    page_url = "shop/cart"

    def check_header_title(self, title):
        header_title = self.find(LocatorsCart.HEADER_TITLE)
        assert header_title.text == title, "заголовок корзины изменился"

    def check_alert_message_empty_cart(self, alert):
        alert_message = self.find(LocatorsCart.ALERT_MESSAGE)
        assert alert_message.text == alert, "изменился alert в пустой корзине"

    def add_to_cart(self):
        self.driver.get(self.base_url)

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(LocatorsCart.PRODUCTS_TITLE))
        product = self.find_all(LocatorsCart.PRODUCTS_TITLE)[0]
        text_product = self.find_all(LocatorsCart.PRODUCTS_TITLE)[0].text
        product.click()

        wait.until(EC.presence_of_element_located(LocatorsCart.BUTTON_ADD))
        self.find(LocatorsCart.BUTTON_ADD).click()

        wait.until(EC.presence_of_element_located(LocatorsCart.BUTTON_CONTINUE))
        self.find(LocatorsCart.BUTTON_CONTINUE).click()

        wait.until(EC.text_to_be_present_in_element(LocatorsCart.QUANTITY_IN_CART, "1"))

        self.find(LocatorsCart.BUTTON_CART).click()
        return text_product

    def check_product_in_cart(self, product):
        assert product in self.find(LocatorsCart.TITLE_PRODUCT_IN_CART).text, "товар в корзине не найден либо не тот"

    def check_block_total_summ_product_in_cart(self):
        assert self.find(LocatorsCart.BLOCK_SUMM).is_displayed(), "блок суммы товаров не отображается"

    def check_block_total_summ_fields(self):
        assert self.find(LocatorsCart.SUBTOTAL).text == "Subtotal"
        assert self.find(LocatorsCart.DISCOUNT_FIELD).is_displayed(), "нет поля ввода discount code"

    def check_alert_input_invalid_discount_code(self, code):
        self.find(LocatorsCart.DISCOUNT_FIELD).send_keys(code)
        self.find(LocatorsCart.BUTTON_APPLY).click()
        assert self.find(LocatorsCart.ALERT_NO_DISCOUNT).text == "This promo code is not available."
