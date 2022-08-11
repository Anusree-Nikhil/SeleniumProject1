from selenium import webdriver
import time
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://login.yahoo.com/?.intl=in")
print("Title of First Window : ", driver.title)  #To print the title of First window
driver.find_element_by_class_name("privacy").click()  #By clicking privacy it will open a new tab
time.sleep(5)
driver.switch_to.window(driver.window_handles[1]) #Where window_handles[1] is the second window
print("Title of Secon Window : ", driver.title)
driver.switch_to.window(driver.window_handles[0]) #Where window_handles[0] is the first window
print(driver.window_handles)
