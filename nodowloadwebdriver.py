from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager   #It allows to download and said the browser driver binaries without us
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.close()


#OR


"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service('C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver')
driver=webdriver.Chrome(service=service_obj)
#driver.close()"""