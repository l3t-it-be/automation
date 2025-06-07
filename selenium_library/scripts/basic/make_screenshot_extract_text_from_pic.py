import os

import pytesseract
from PIL import Image

from selenium_library.browser_setup import browser

with browser:
    browser.get('https://parsinger.ru/selenium/6/6.2.1/index.html')

    picture = browser.find_element('css selector', '#this_pic')

    os.makedirs('files/images', exist_ok=True)
    picture.screenshot('files/images/screenshot.png')

    image = Image.open('files/images/screenshot.png')
    code = pytesseract.image_to_string(image)
    print('Code from picture:', code)
