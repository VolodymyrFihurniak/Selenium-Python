from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    @staticmethod
    def check_the_title_of_the_book(first, second):
        assert first.text == second.text, 'Different product name'

    @staticmethod
    def check_price(first, second):
        assert first.text in second.text, 'Different product price'

    def add_to_cart(self):
        self.find_element(*MainPageLocators.ADD_TO_CART).click()
        self.solve_quiz_and_get_code()
        self.check_the_title_of_the_book(self.find_element(*MainPageLocators.FIRST_NAME_BOOK),
                                         self.find_element(*MainPageLocators.SECOND_NAME_BOOK))
        self.check_price(self.find_element(*MainPageLocators.FIRST_MONEY_BOOK),
                         self.find_element(*MainPageLocators.SECOND_MONEY_BOOK))

    def add_to_cart_and_check_is_not_element_present(self):
        self.find_element(*MainPageLocators.ADD_TO_CART).click()
        self.solve_quiz_and_get_code()
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), 'Error is not element present'

    def check_is_not_element_present(self):
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), 'Error is not element present'

    def add_to_cart_and_check_is_disappeared(self):
        self.find_element(*MainPageLocators.ADD_TO_CART).click()
        self.solve_quiz_and_get_code()
        assert self.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE), 'Error is disappeared'
