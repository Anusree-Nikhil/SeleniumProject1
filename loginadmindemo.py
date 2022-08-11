from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver.exe')
driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
from selenium.webdriver.common.by import By

"""class demoCheckbox():
    def demo_check(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver.exe')
        driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')"""

username=driver.find_element(by=By.NAME,value='Email')
username.send_keys('')
password=driver.find_element(by=By.NAME,value='Password')
password.send_keys('')
check_box=driver.find_element(by=By.NAME,value='RememberMe')
check_box.click()
submitbutton=driver.find_element_by_xpath("//button[@type='submit']")
submitbutton.click()

print(driver.title)

extitle='Dashboard / nopCommerce administration'
ctitle=driver.title
if extitle==ctitle:
    print('tested successfully')
else:
    print('testing failed')