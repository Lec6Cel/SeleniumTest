from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.conferenceseries.com/past-conference-reports.php")

result = driver.find_elements(By.CSS_SELECTOR,".list-group .list-group-item")

for it in result[:10]:
    title = it.get_attribute("title")
    date_country = it.find_elements(By.CLASS_NAME,"col-md-3")
    date = date_country[0].text
    country = date_country[1].text

    print(title)
    print(date)
    print(country)
    print("=======")
driver.quit()
