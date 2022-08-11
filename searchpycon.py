from selenium import webdriver
driver=webdriver.Chrome('C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver')
driver.get("https://www.python.org/")
from selenium.webdriver.common.by import By
search=driver.find_element(by=By.NAME,value='q')
search.send_keys("Pycon")
go_button=driver.find_element(by=By.ID,value='submit')
go_button.click()

print(driver.title)

extitle='Welcome to Python.org'
captit=driver.title
if extitle==captit:
    print("Tested successfully")
else:
    print('Testing failed')