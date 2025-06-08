import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox',
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: ',
        # fmt: off
        choices=('ar', 'ca', 'cs', 'da', 'de', 'en', 'el',
                 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl',
                 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans')
        # fmt: on
    )


def setup_browser(browser_name, language):
    if browser_name == 'chrome':
        print('\nStart Chrome browser for test')
        service = ChromeService(
            executable_path=ChromeDriverManager().install()
        )
        driver_options = webdriver.ChromeOptions()
    elif browser_name == 'firefox':
        print('\nStart Firefox browser for test')
        service = FirefoxService(
            executable_path=GeckoDriverManager().install()
        )
        driver_options = webdriver.FirefoxOptions()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--start-maximized')
    driver_options.add_argument('--disable-extensions')
    driver_options.add_argument('--disable-popup-blocking')
    driver_options.add_argument('--headless=new')

    if browser_name == 'chrome':
        driver_options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
        browser = webdriver.Chrome(service=service, options=driver_options)
    else:
        driver_options.set_preference('intl.accept_languages', str(language))
        browser = webdriver.Firefox(service=service, options=driver_options)

    return browser


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    browser = setup_browser(browser_name, language)
    browser.implicitly_wait(10)

    yield browser
    print('\nQuit browser after test')
    browser.quit()


@pytest.fixture()
def random_generator():
    return Faker()
