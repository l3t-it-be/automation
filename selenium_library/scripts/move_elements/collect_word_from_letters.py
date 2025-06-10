from selenium.webdriver import ActionChains

from selenium_library.browser_setup import browser

with browser:
    browser.set_window_size(1920, 1080)  # necessity for headless mode
    browser.get('https://parsinger.ru/draganddrop/4/index.html')

    target_word = browser.find_element('css selector', '#target-word').text
    word_as_letters = list(target_word)

    all_letters = browser.find_elements(
        'css selector', '#alphabet .draggable-letter'
    )
    all_letters_dict = {letter.text: letter for letter in all_letters}

    targets = browser.find_elements(
        'css selector', '#letter-slots .letter-slot'
    )

    actions = ActionChains(browser)
    for letter, target in zip(word_as_letters, targets):
        actions.drag_and_drop(all_letters_dict[letter], target).perform()

    password = browser.find_element('css selector', '#password').text
    print(password)
