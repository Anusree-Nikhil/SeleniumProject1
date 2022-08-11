from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver.exe")
driver.get("https://www.freelancer.com/post-project")

ele=driver.find_element_by_class_name("NativeElement")
print("element is displayed: " +str(ele.is_displayed()))

