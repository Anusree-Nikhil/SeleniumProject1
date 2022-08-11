from selenium import webdriver
#from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#driver.implicitly_wait(10)
from selenium.webdriver.common.by import By

driver.switch_to.frame("packageListFrame")
frame1content = driver.find_element(By.LINK_TEXT, "org.openqa.selenium.bidi.log")
frame1content.click()
driver.maximize_window()
#driver.minimize_window()
driver.switch_to.default_content()
time.sleep(5)

driver.switch_to.frame("packageFrame")
frame2content = driver.find_element(By.LINK_TEXT,"ConsoleLogEntry")
frame2content.click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
frame3content=driver.find_element(By.XPATH,value="/html/body/header/nav/div[1]/div[1]/ul/li[4]")
frame3content.click()
driver.switch_to.default_content()