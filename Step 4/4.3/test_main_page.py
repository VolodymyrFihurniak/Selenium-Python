from section_2.pages.main_page import MainPage
from section_2.pages.login_page import LoginPage

import pytest


@pytest.mark.login
class TestLoginFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser

    def test_user_should_see_login_link(self):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(self.browser, link)
        page.open()
        page.should_be_login_link()

    def test_user_can_go_to_login_page(self):
        link = 'http://selenium1py.pythonanywhere.com'
        page = MainPage(self.browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.product
class TestProductFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser

    def test_user_cant_see_product_in_basket_opened_from_main_page(self):
        link = 'http://selenium1py.pythonanywhere.com'
        page = MainPage(self.browser, link)
        page.open()
        page.go_to_cart()
        page.check_for_missing_items_in_the_cart()
        page.we_expect_that_the_basket_has_a_text_about_the_absence_of_goods()