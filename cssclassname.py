from selenium import webdriver
driver=webdriver.Chrome("c:\\Users\\Anju Anil\\Desktop\\Python\\chromedriver")
driver.get("https://www.facebook.com/login/")
from selenium.webdriver.common.by import By

username=driver.find_element(by=By.CSS_SELECTOR,value="input.inputtext")
username.send_keys('anusree265@gmail.com')
password=driver.find_element(by=By.CSS_SELECTOR,value="input#pass")
password.send_keys('anusreemanu')
login=driver.find_element(by=By.CSS_SELECTOR,value="button#loginbutton")
login.click()

