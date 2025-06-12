import os

import pydub
import requests
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from twocaptcha import TwoCaptcha

import speech_recognition as sr

from selenium_library.browser_setup import browser

solver = TwoCaptcha('*****************')
results_dict = {}
reported_captcha_ids = set()

audio_dir = 'files/audio'
audio_file_mp3 = os.path.join(audio_dir, 'audio_captcha.mp3')
audio_file_wav = os.path.join(audio_dir, 'audio_captcha.wav')


def send_captcha(captcha_type: str, captcha) -> str:
    print('Sending captcha for solving...')
    result = None

    if captcha_type == 'img':
        result = solver.normal(captcha)
    elif captcha_type == 'text':
        result = solver.text(captcha)

    print(f'Captcha solved: {result["code"]}')
    results_dict.update(result)
    return result['code']


def solve_captcha(captcha_type) -> None:
    captcha_input = browser.find_element('css selector', '.chakra-input')
    submit_button = browser.find_element(
        'css selector', 'button.chakra-button.css-1wq39mj'
    )
    print('Solving captcha...')

    if captcha_type == 'img':
        captcha_picture = browser.find_element(
            'css selector', '.chakra-form-control img'
        )

        os.makedirs('files/images', exist_ok=True)
        path = 'files/images/image.png'
        captcha_picture.screenshot(path)
        captcha_input.send_keys(send_captcha(captcha_type, path))

    elif captcha_type == 'text':
        captcha_text = browser.find_element(
            'css selector', '.chakra-form-control p'
        ).text
        captcha_input.send_keys(send_captcha(captcha_type, captcha_text))

    submit_button.click()


def report_captcha_result(captcha_id: str, is_correct: bool):
    if captcha_id not in reported_captcha_ids:
        try:
            solver.report(captcha_id, is_correct)
            reported_captcha_ids.add(captcha_id)
            status = 'success' if is_correct else 'failure'
            print(f'Reported {status} for captchaId: {captcha_id}')
        except Exception as e:
            print(f'Error reporting captcha: {e}')


def download_audio(url) -> None:
    os.makedirs(audio_dir, exist_ok=True)
    response = requests.get(url)
    with open(audio_file_mp3, 'wb') as file:
        file.write(response.content)


def audio_to_text() -> str:
    sound = pydub.AudioSegment.from_file(audio_file_mp3, 'mp3')
    sound.export(audio_file_wav, format='wav')

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_wav) as source:
        audio = recognizer.record(source)

    return recognizer.recognize_google(audio, language='en-US')


def solve_recaptcha() -> None:
    try:
        WebDriverWait(browser, 10).until(
            ec.frame_to_be_available_and_switch_to_it(
                ('css selector', 'iframe[title="reCAPTCHA"]')
            )
        )
        WebDriverWait(browser, 10).until(
            ec.element_to_be_clickable(('css selector', '#recaptcha-anchor'))
        ).click()

        browser.switch_to.default_content()

        WebDriverWait(browser, 10).until(
            ec.frame_to_be_available_and_switch_to_it(
                (
                    'css selector',
                    'iframe[title*="текущую проверку reCAPTCHA"]',
                )
            )
        )
        WebDriverWait(browser, 10).until(
            ec.element_to_be_clickable(
                ('css selector', '#recaptcha-audio-button')
            )
        ).click()

        audio_src = browser.find_element(
            'css selector', '#audio-source'
        ).get_attribute('src')
        download_audio(audio_src)

        text = audio_to_text()
        input_field = browser.find_element('css selector', '#audio-response')
        input_field.send_keys(text.lower())
        input_field.send_keys(Keys.ENTER)

        browser.switch_to.default_content()

    except Exception as e:
        print(f'Ошибка при обходе капчи: {e}')


def solve_yandex_captcha():
    WebDriverWait(browser, 10).until(
        ec.frame_to_be_available_and_switch_to_it(
            ('css selector', 'iframe[title="SmartCaptcha checkbox widget"]')
        )
    )
    WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable(
            ('css selector', 'input[class="CheckboxCaptcha-Button"]')
        )
    ).click()

    browser.switch_to.default_content()

    WebDriverWait(browser, 10).until(
        ec.frame_to_be_available_and_switch_to_it(
            ('css selector', 'iframe[title="SmartCaptcha advanced widget"]')
        )
    )
    img_url = browser.find_element(
        'css selector', 'div.AdvancedCaptcha-View img'
    ).get_attribute('src')

    os.makedirs('files/images', exist_ok=True)

    path = 'files/images/yandex_img.png'

    with open(path, 'wb') as file:
        file.write(requests.get(img_url).content)
    print('Captcha img saved')

    captcha_text = send_captcha('img', path)

    browser.find_element(
        'css selector', 'input[class="Textinput-Control"]'
    ).send_keys(captcha_text)

    browser.find_element(
        'css selector', 'button[class]:not([class=""])'
    ).click()

    browser.switch_to.default_content()
