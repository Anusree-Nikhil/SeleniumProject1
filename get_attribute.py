from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver.exe")
driver.get("https://www.geeksforgeeks.org/")

ele=driver.find_element_by_link_text("Courses")
print(ele.get_attribute("href"))