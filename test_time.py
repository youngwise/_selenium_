import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

@pytest.fixture(scope='function')
def browser():
    print('Начало теста...')
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("Конец теста")
    browser.quit()
    return browser

@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
class TestTime():
    def test_url(self, browser, link):
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(str(answer))
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
        text = WebDriverWait(browser, 12).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))
        )
        assert text.text == 'Correct!', f'"{text.text}" не совпадает со строкой "Correct!"'
        time.sleep(5)
