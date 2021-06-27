def test_guest_should_see_login_link(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-add-to-basket"]').submit()
    assert 'Coders at Work' in browser.find_element_by_class_name('alertinner').text, 'Error adding item to cart'
