from selenium import webdriver
import time
import unittest

text = {0: 'first', 1: 'second', 2: 'third'}

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def test(link):
    global welcome_text
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.get(link)

    elements = browser.find_elements_by_xpath("//label[contains(text(), '*')]")
    for element in range(len(elements)):
        browser.find_element_by_css_selector(f'.first_block  input.{text[element]}').send_keys(text[element])

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    time.sleep(3)
    browser.quit()

class TestAbs(unittest.TestCase):

    def test_1(self):
        test(link1)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_2(self):
        test(link2)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
