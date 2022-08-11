from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get('https://opensource-demo.orangehrmlive.com/')
from selenium.webdriver.common.by import By  #Identify the path of the locator id or class is used to loacate elements within a document
user_name_Input=driver.find_element(by=By.CSS_SELECTOR,value='input[name=txtUsername]')
user_name_Input.send_keys('Admin')
password_Input=driver.find_element(by=By.CSS_SELECTOR,value='input[name=txtPassword]')
password_Input.send_keys('admin123')
login_Button=driver.find_element(by=By.CSS_SELECTOR,value='input[name=Submit]')
login_Button.click()