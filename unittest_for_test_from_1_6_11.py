from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

text = {0: 'first', 1: 'second', 2: 'third'}

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestAbs(unittest.TestCase):

    def test_1(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser.get(link1)

        elements = browser.find_elements(By.XPATH, "//label[contains(text(), '*')]")
        for element in range(len(elements)):
            browser.find_element(By.CSS_SELECTOR, f'.first_block  input.{text[element]}').send_keys(text[element])

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(2)
        browser.quit()

    def test_2(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser.get(link2)

        elements = browser.find_elements(By.XPATH, "//label[contains(text(), '*')]")
        for element in range(len(elements)):
            browser.find_element(By.CSS_SELECTOR, f'.first_block  input.{text[element]}').send_keys(text[element])

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(2)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
