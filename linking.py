from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.python.org/")

link=driver.find_element_by_link_text("docs.python.org")
link.click()