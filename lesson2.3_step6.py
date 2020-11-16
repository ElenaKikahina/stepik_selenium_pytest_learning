from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

journey_button = browser.find_element_by_class_name("btn-primary").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

time.sleep(1)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
#time.sleep(3)

answer_field = browser.find_element_by_id("answer")
answer_field.send_keys(y)

submit_button = browser.find_element_by_css_selector("[type='submit']").click()
time.sleep(10)
browser.quit()
