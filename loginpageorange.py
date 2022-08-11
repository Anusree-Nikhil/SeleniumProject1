from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get('https://opensource-demo.orangehrmlive.com/')
from selenium.webdriver.common.by import By  #Identify the path of the locator id or class is used to loacate elements within a document
user_name_Input=driver.find_element(by=By.NAME,value='txtUsername')
user_name_Input.send_keys('Admin')
password_Input=driver.find_element(by=By.NAME,value='txtPassword')
password_Input.send_keys('admin123')
login_Button=driver.find_element(by=By.NAME,value='Submit')
login_Button.click()
expected_title="OrangeHRM"
captured_title=driver.title
if expected_title==captured_title:
    print('Tested successfully')
else:
    print('Testing failed')


