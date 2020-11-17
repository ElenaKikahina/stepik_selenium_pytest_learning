from selenium import webdriver
import os
import time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name_field = browser.find_element_by_name("firstname").send_keys("Tom")
last_name_field = browser.find_element_by_name("lastname").send_keys("Stone")
email_field = browser.find_element_by_name("email").send_keys("test@gmail.com")

choose_file_button = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
choose_file_button.send_keys(file_path)

submit_button = browser.find_element_by_css_selector("[type='submit']").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
