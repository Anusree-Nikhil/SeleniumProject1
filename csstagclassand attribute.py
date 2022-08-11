from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.facebook.com/login/")
from selenium.webdriver.common.by import By

username=driver.find_element(by=By.CSS_SELECTOR,value='input.inputtext[name=email]').send_keys('anusree265@gmail.com')
password=driver.find_element(by=By.CSS_SELECTOR,value='input.inputtext[name=pass]').send_keys('anusreemanu')
login=driver.find_element(by=By.CSS_SELECTOR,value='button._42ft[id=loginbutton]').click()