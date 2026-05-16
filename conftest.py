import pytest
from selenium import webdriver
# from pages.customer_login_less27 import CustomerLogin
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver_chrome = webdriver.Chrome(options=options)
    # driver_chrome.maximize_window()
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
