from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_should_see_login_link(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]').submit()
    value = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'alertinner')))
    assert 'Coders at Work' in value.text, 'Error adding item to cart'
