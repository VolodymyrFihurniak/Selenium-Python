from section_2.pages.basket_page import BasketPage
from section_2.pages.product_page import ProductPage
from section_2.pages.login_page import LoginPage

import pytest
import time


@pytest.mark.login
class TestLoginFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(self.browser, link)
        page.open()
        page.go_to_the_login_page()

    def test_user_should_see_login_link_on_product_page(self):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.product
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(self.browser, link)
        page.open()
        page.register_new_user(str(time.time()) + '@gmail.com', 'FatRat131#!4')

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_cart()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self):
        page = ProductPage(self.browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/', 0)
        page.open()
        page.add_to_cart_and_check_is_not_element_present()

    def test_message_disappeared_after_adding_product_to_basket(self):
        page = ProductPage(self.browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/', 0)
        page.open()
        page.add_to_cart_and_check_is_disappeared()


@pytest.mark.product
class TestProductFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/', 0)
        page.open()
        page.check_is_not_element_present()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                           "/?promo=offer7", marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, link):
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_cart()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        link = 'http://selenium1py.pythonanywhere.com'
        page = BasketPage(self.browser, link)
        page.open()
        page.go_to_cart()
        page.check_for_missing_items_in_the_cart()
        page.we_expect_that_the_basket_has_a_text_about_the_absence_of_goods()
