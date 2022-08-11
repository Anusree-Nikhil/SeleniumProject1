from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")

mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException])
driver.get("https://www.facebook.com/login/")
driver.maximize_window()
username=mywait.until(ec.presence_of_element_located((By.XPATH,"//input[@id='email']")))
username.send_keys('haaii')
#driver.quit()