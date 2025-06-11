from fake_useragent import UserAgent
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ua = UserAgent()


def create_driver():
    service = Service(executable_path=ChromeDriverManager().install())

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--incognito')
    driver_options.add_argument('--disable-notifications')
    driver_options.add_argument('--ignore-certificate-errors')
    driver_options.add_argument(f'user-agent={ua.random}')
    driver_options.add_argument('--headless=new')
    driver = webdriver.Chrome(
        service=service,
        options=driver_options,
    )
    driver.implicitly_wait(10)
    return driver


browser = create_driver()
random_generator = Faker()
