from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
from selenium.webdriver.common.by import By
driver.maximize_window()

rows=driver.find_elements(by=By.XPATH, value="//table[@name='BookTable']//tr")
columns=driver.find_elements(by=By.XPATH, value="//table[@name='BookTable']//tr[1]/th")
print("Number of rows: ", len(rows))
print("Number of columns :", len(columns))