from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    
    # Отправляем заполненную форму
    dis = button.get_attribute("disabled")
    if dis!="disabled":
        button.click()
        # ожидание
        time.sleep(10)
    else:
        assert "Error"
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

