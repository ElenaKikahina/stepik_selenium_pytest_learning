from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x, y):
    return str(int(x) + int(y))

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text
z = calc(x, y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(z)
time.sleep(3)
submit_button = browser.find_element_by_css_selector("[type='submit']").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()


