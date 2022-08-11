import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver.exe")
driver.get("https://www.facebook.com/login/")
#driver.implicitly_wait(10)

username=driver.find_element_by_class_name("inputtext").send_keys("anusree265@gmail.com")
password=driver.find_element_by_id("pass").send_keys("anusreemanu")
login=driver.find_element_by_id("loginbutton").click()

try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@type='search']")))
    element.send_keys('sherin mariyamma')
    element.send_keys(Keys.ENTER)
    time.sleep(10)
finally:
    time.sleep(10)
    #driver.close()
