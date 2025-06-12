import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())

driver_options = webdriver.ChromeOptions()
driver_options.page_load_strategy = 'eager'

download_dir = os.path.join(os.getcwd(), 'files', 'downloads')
os.makedirs(download_dir, exist_ok=True)
prefs = {'download.default_directory': download_dir}
driver_options.add_experimental_option('prefs', prefs)
print(f'Download dir: {download_dir}')

browser = webdriver.Chrome(service=service, options=driver_options)
browser.implicitly_wait(10)


def downloads_done(folder):
    for fname in os.listdir(folder):
        if fname.endswith(('.crdownload', '.tmp', '.part')):
            return False
    return True


with browser:
    browser.get('https://the-internet.herokuapp.com/download')
    links = browser.find_elements('css selector', '.example a')
    filenames = [
        os.path.basename(link.get_attribute('href')) for link in links
    ]
    total = len(filenames)

    for idx, (link, filename) in enumerate(zip(links, filenames), start=1):
        link.click()
        print(f'{idx} / {total} {filename} downloaded successfully')

    while not downloads_done(download_dir):
        time.sleep(1)

    upload_dir = os.path.join(os.getcwd(), 'files', 'downloads')

    files_to_upload = [
        os.path.join(upload_dir, file)
        for file in os.listdir(upload_dir)
        if os.path.isfile(os.path.join(upload_dir, file))
        and not file.endswith(('.crdownload', '.tmp', '.part'))
    ]

    for filepath in files_to_upload:
        browser.get('https://the-internet.herokuapp.com/upload')

        file_input = browser.find_element('css selector', '[type="file"]')
        file_input.send_keys(filepath)

        submit_btn = browser.find_element('css selector', '[type="submit"]')
        submit_btn.click()

        print(f'Uploaded {os.path.basename(filepath)}')
        time.sleep(1)
