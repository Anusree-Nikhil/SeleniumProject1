from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
button=driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Prompt']")
button.click()
time.sleep(10)
a_window=driver.switch_to.alert
print(a_window.text)
a_window.accept()
#a_window.dismiss()