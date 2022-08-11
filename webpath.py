from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver')
driver.get('https://www.python.org/') #Code to find a particular page
driver.close()  #This code closes the browser fastly