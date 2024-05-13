from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://vnexpress.net/")

driver.implicitly_wait(3)
result = driver.find_elements(By.CSS_SELECTOR, "#automation_TV0 article.item-news")

for it in result[:10]:
        title_new = it.find_element(By.CLASS_NAME, "title-news").text
        des = it.find_element(By.CLASS_NAME, "description").text
        img = it.find_element(By.CLASS_NAME, "thumb-art img").get_attribute("src")
        print(title_new)
        print(des)
        print(img)
        print("===========")

driver.quit()
