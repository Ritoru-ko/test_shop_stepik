import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    lan= request.config.getoption("language")
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': lan})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

