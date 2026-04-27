from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.locators_cart import LocatorsCategory


class CategoryPage(BasePage):
    page_url = "shop/category/desks-1"

    def search_in_category_positive(self, product):
        wait = WebDriverWait(self.driver, 5)

        wait.until(EC.presence_of_element_located(LocatorsCategory.FIELDS_SEARCH))
        search_field = self.find_all(LocatorsCategory.FIELDS_SEARCH)[1]

        search_field.send_keys(product)

        self.find(LocatorsCategory.BUTTON_GLASS).click()

        wait.until(EC.text_to_be_present_in_element(LocatorsCategory.PRODUCTS_TITLE, product))
        text_product = self.find(LocatorsCategory.PRODUCTS_TITLE).text

        assert text_product == product

    def search_in_category_negative(self, product):
        wait = WebDriverWait(self.driver, 5)

        wait.until(EC.presence_of_element_located(LocatorsCategory.FIELDS_SEARCH))
        search_field = self.find_all(LocatorsCategory.FIELDS_SEARCH)[1]

        search_field.clear()
        search_field.send_keys(product)

        self.find(LocatorsCategory.BUTTON_GLASS).click()

        wait.until(EC.presence_of_element_located(LocatorsCategory.MESS_NO_RESULT))
        text_no_results = self.find(LocatorsCategory.MESS_NO_RESULT).text
        text_under_no_results = self.find(LocatorsCategory.MESS_NO_RESULT_UNDER).text

        assert text_no_results == "No results"
        assert text_under_no_results == f'No results for "{product}" in category "Desks".'

    def filter_by_legs(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(LocatorsCategory.PRICE_RANGE))

        self.find(LocatorsCategory.CHECKBOX_ALUM).click()

    def check_after_filter(self):
        count_product = len(self.find_all(LocatorsCategory.PRODUCT_IMAGES))
        text_product = self.find(LocatorsCategory.PRODUCTS_TITLE).text

        assert count_product == 1
        assert text_product == "Customizable Desk"

    def switch_currency_eur(self):
        wait = WebDriverWait(self.driver, 5)

        switcher_pricelist = self.find(LocatorsCategory.SWITCHER_PRICELIST)
        switcher_pricelist.click()

        wait.until(EC.element_to_be_clickable(LocatorsCategory.SWITCHER_EUR))
        eur = self.find(LocatorsCategory.SWITCHER_EUR)
        eur.click()

    def check_currency_product(self, currency):
        assert currency in self.find(LocatorsCategory.PRODUCT_PRICE).text

    def check_field_switch_currency(self):
        switcher_pricelist = self.find(LocatorsCategory.SWITCHER_PRICELIST)
        assert switcher_pricelist.is_displayed(), "поле выбора валюты не отображается"
