import requests
from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
from  selenium.webdriver.common.by import By
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

links=driver.find_elements(by=By.TAG_NAME,value='a')
print("Broken codes: ")
good_links=[]

for link in links:
    url=link.get_attribute("href")
    try:
        res=requests.head(url)
        if res.status_code >= 400:
            print(url)
        else:
            good_links.append(url)
            print("Good links :   ", good_links)
    except:
        None

