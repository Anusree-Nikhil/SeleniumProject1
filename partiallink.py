from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.python.org/")

plink=driver.find_element_by_partial_link_text("All")
plink.click()