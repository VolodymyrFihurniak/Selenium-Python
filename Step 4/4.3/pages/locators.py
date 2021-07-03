from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    FIRST_NAME_BOOK = (By.TAG_NAME, 'h1')
    SECOND_NAME_BOOK = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    FIRST_MONEY_BOOK = (By.CSS_SELECTOR, '.product_main .price_color')
    SECOND_MONEY_BOOK = (By.CSS_SELECTOR, '.alert .alertinner p:first-child')
    ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@class="alertinner "]//strong[text()="Deferred benefit offer"]')
    CART_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    LIST_OF_GOODS = (By.XPATH, '//*[@id="basket_formset"]/div/div')
    TEXT_ABOUT_THE_MISSING = (By.XPATH, '//*[@id="content_inner"]/p')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    LIST_OF_GOODS = (By.XPATH, '//*[@id="basket_formset"]/div/div')
    TEXT_ABOUT_THE_MISSING = (By.XPATH, '//*[@id="content_inner"]/p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginAndRegisterPageLocators:
    REGISTER_EMAIL_INPUT = (By.NAME, 'registration-email')
    REGISTER_PASSWORD_ONE_INPUT = (By.NAME, 'registration-password1')
    REGISTER_PASSWORD_TWO_INPUT = (By.NAME, 'registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div/div')
