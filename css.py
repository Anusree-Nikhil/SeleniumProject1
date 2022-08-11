from selenium import webdriver
driver=webdriver.Chrome("c:\\Users\\Anju Anil\\Desktop\\Python\\chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
from selenium.webdriver.common.by import By

username_Input=driver.find_element(by=By.CSS_SELECTOR,value='input#txtUsername')
username_Input.send_keys("Admin")
password_Input=driver.find_element(by=By.CSS_SELECTOR,value="input#txtPassword")
password_Input.send_keys("admin123")
login_button=driver.find_element(by=By.CSS_SELECTOR,value="input#btnLogin")
login_button.click()