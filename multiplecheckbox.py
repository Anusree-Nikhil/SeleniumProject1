from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox==checkboxes[1]:
        pass
    else:
        checkbox.click()
print(len(checkboxes))