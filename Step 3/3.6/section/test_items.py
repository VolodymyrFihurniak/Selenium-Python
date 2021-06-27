from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart_button_is_displayed(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')),
        'Error find button')
    assert button, 'Error find button'
