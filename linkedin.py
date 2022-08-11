from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.google.com/")

search=driver.find_element_by_name("q")
search.send_keys("LinkedIn Login")
search.send_keys(Keys.ENTER)
driver.find_element_by_class_name("LC20lb").click()