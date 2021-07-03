import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language. Example: ru, ua, en, es')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language').lower()
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        option = ChromeOptions()
        option.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        with webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver',
                              options=option) as browser:
            yield browser
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        option = webdriver.FirefoxProfile()
        option.set_preference('intl.accept_languages', user_language)
        with webdriver.Firefox(executable_path=os.path.join(os.getcwd(), '../webdriver/geckodriver'),
                               firefox_profile=option) as browser:
            yield browser
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
