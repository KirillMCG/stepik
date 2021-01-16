from selenium import webdriver
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
#    browser.implicitly_wait(5)

    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    button2 = browser.find_element_by_css_selector("body > form > div > div > button")
    button2.click()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()