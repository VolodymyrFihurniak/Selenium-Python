from .main_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def go_to_cart(self):
        self.find_element(*BasePageLocators.CART_LINK).click()

    def check_for_missing_items_in_the_cart(self):
        self.is_not_element_present(*BasePageLocators.LIST_OF_GOODS)

    def we_expect_that_the_basket_has_a_text_about_the_absence_of_goods(self):
        self.is_element_present(*BasePageLocators.TEXT_ABOUT_THE_MISSING)
