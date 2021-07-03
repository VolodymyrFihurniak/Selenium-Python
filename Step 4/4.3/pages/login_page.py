from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginAndRegisterPageLocators


class LoginPage(BasePage, MainPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'accounts/login/' in self.url, 'Invalid login link'
        return True

    def should_be_login_form(self):
        assert self.is_element_present(*self.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*self.REGISTER_FORM)

    def register_new_user(self, email, password):
        if self.should_be_login_url():
            self.find_element(*LoginAndRegisterPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
            self.find_element(*LoginAndRegisterPageLocators.REGISTER_PASSWORD_ONE_INPUT).send_keys(password)
            self.find_element(*LoginAndRegisterPageLocators.REGISTER_PASSWORD_TWO_INPUT).send_keys(password)
            self.find_element(*LoginAndRegisterPageLocators.REGISTER_SUBMIT).click()
            if self.is_element_present(*LoginAndRegisterPageLocators.SUCCESS_MESSAGE):
                assert 'Thanks for registering!' in self.find_element(*LoginAndRegisterPageLocators.SUCCESS_MESSAGE
                                                                      ).text, 'Failed to register user. ' \
                                                                              'This user may ' \
                                                                              'already be registered'
            else:
                assert False, 'Failed to register user. This user may already be registered'
