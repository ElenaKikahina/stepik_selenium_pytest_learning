from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(y)
checkbox = browser.find_element_by_id("robotCheckbox").click()
radiobutton = browser.find_element_by_id("robotsRule").click()
time.sleep(3)
submit_button = browser.find_element_by_css_selector("[type='submit']").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
