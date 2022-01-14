from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # browser.find_element_by_css_selector("[type='submit']").click()
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    # confirm = browser.switch_to.alert
    # confirm.accept()

    text = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    if text:
        browser.find_element_by_id("book").click()

    x = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(calc(x))
    # browser.find_element_by_id("robotCheckbox").click()
    # element = browser.find_element_by_id("robotsRule")
    # browser.execute_script('return arguments[0].scrollIntoView(true);', element)
    # element.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
