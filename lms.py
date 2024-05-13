import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

kw = input("nhap mssv: ")
pw = input("nhap mat khau: ")
driver = webdriver.Chrome()
driver.get("https://lms.ou.edu.vn/")
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME, "main-btn").click()
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME, "login100-form-btn").click()

driver.implicitly_wait(5)
user_type = Select(driver.find_element(By.ID,"form-usertype"))
user_type.select_by_index(0)

username = driver.find_element(By.ID,"form-username")
password = driver.find_element(By.ID, "form-password")

username.send_keys(kw)

password.send_keys(pw)

driver.find_element(By.CLASS_NAME,"m-loginbox-submit-btn").click()

driver.quit()
