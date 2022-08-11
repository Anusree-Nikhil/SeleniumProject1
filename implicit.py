from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver.exe")
driver.get("https://www.facebook.com/login/")
driver.implicitly_wait(10)

username=driver.find_element_by_class_name("inputtext").send_keys("anusree265@gmail.com")
password=driver.find_element_by_id("pass").send_keys("anusreemanu")
login=driver.find_element_by_id("loginbutton").click()