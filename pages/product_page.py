from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.locators_cart import LocatorsProduct


class ProductPage(BasePage):
    page_url = "shop/furn-9999-office-design-software-7?category=9"

    def check_title_product(self, title):
        title_product = self.find(LocatorsProduct.TITLE_PRODUCT).text
        assert title_product == title

    def check_currency_value(self):
        currency_value = self.find(LocatorsProduct.CURRENCY_VALUE)
        assert currency_value.is_displayed()
        assert float(currency_value.text) > 0

    def check_field_count_and_add(self):
        assert self.find(LocatorsProduct.BUTTON_REMOVE).is_displayed()
        assert self.find(LocatorsProduct.BUTTON_ADD).is_displayed()
        assert self.find(LocatorsProduct.FIELD_COUNT).is_displayed()
        assert self.find(LocatorsProduct.BUTTON_ADD).is_displayed()

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        self.find(LocatorsProduct.BUTTON_ADD_CART).click()
        wait.until(EC.text_to_be_present_in_element(LocatorsProduct.QUANTITY_IN_CART, "1"))
        self.find(LocatorsProduct.BUTTON_CART).click()

    def check_product_in_cart(self):
        assert self.find(LocatorsProduct.TITLE_PRODUCT_IN_CART).text == "Office Design Software"

    def field_search(self, product):
        wait = WebDriverWait(self.driver, 5)

        wait.until(EC.presence_of_element_located(LocatorsProduct.FIELDS_SEARCH))
        search_field = self.find_all(LocatorsProduct.FIELDS_SEARCH)[1]

        search_field.send_keys(product)

        self.find(LocatorsProduct.BUTTON_GLASS).click()

    def check_no_results_after_search(self, product):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(LocatorsProduct.MESS_NO_RESULT))
        text_no_results = self.find(LocatorsProduct.MESS_NO_RESULT).text
        text_under_no_results = self.find(LocatorsProduct.MESS_NO_RESULT_UNDER).text

        assert text_no_results == "No results"
        assert text_under_no_results == f'No results for "{product}" in category "Multimedia".'
