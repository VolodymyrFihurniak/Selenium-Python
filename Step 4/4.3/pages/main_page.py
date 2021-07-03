from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def check_is_not_element_present(self):
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)

    def go_to_cart(self):
        self.find_element(*MainPageLocators.CART_LINK).click()

    def check_for_missing_items_in_the_cart(self):
        self.is_not_element_present(*MainPageLocators.LIST_OF_GOODS)

    def we_expect_that_the_basket_has_a_text_about_the_absence_of_goods(self):
        self.is_element_present(*MainPageLocators.TEXT_ABOUT_THE_MISSING)
