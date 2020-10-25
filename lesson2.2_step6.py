from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer_field = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
answer_field.send_keys(y)
#time.sleep(3)

checkbox = browser.find_element_by_id("robotCheckbox").click()
radiobutton = browser.find_element_by_id("robotsRule").click()
#time.sleep(3)
submit_button = browser.find_element_by_css_selector("[type='submit']").click()
time.sleep(3)

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
