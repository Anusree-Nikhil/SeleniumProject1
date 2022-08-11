from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.pendujatt.net/")
from selenium.webdriver.common.by import By

link=driver.find_element_by_link_text("New Punjabi Songs")
link.click()