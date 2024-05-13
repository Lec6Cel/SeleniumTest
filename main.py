from selenium import webdriver
from selenium.webdriver.common.by import By

kw = input("nhap tu khoa: ")
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

el = driver.find_element(By.NAME,"q")
el.send_keys(kw)
el.submit()

driver.implicitly_wait(3)

result = driver.find_elements(By.CSS_SELECTOR,".e2BEnf h3")

for it in result:
    print(it.text)

driver.quit()


