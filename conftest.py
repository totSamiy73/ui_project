import pytest
from selenium import webdriver
# from pages.customer_login_less27 import CustomerLogin
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@pytest.fixture()
def driver():
    driver_chrome = webdriver.Chrome()
    driver_chrome.maximize_window()
    yield driver_chrome
    driver_chrome.quit()


# @pytest.fixture()
# def login(driver):
#     return CustomerLogin(driver)


@pytest.fixture()
def cart(driver):
    return CartPage(driver)


@pytest.fixture()
def category(driver):
    return CategoryPage(driver)


@pytest.fixture()
def product(driver):
    return ProductPage(driver)
