from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
button=driver.find_element(by=By.XPATH,value="//button['Click for JS Confirm']")
button.click()
alert=Alert(driver)
time.sleep(5)
print(alert.text)
alert.accept()