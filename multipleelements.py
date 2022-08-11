from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.yatra.com/")

mul=driver.find_elements_by_tag_name("a")
print(len(mul))
for i in mul:
    print(i.text)