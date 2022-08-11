from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

driver_service=Service("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver=webdriver.Chrome(service=driver_service)
driver.get("https://www.google.com/search?q=facebook&oq=fa&aqs=chrome.0.0i131i355i433i512j46i131i199i433i465i512j69i57j0i131i433i512j46i131i433j0i131i433i512j0i512j69i60.2103j0j7&sourceid=chrome&ie=UTF-8")
from selenium.webdriver.common.by import By

link=driver.find_element_by_link_text("Log In")
link.click()
email=driver.find_element(by=By.NAME,value='email')
email.send_keys('anusree265@gmail.com')
password=driver.find_element(by=By.ID,value='pass')
password.send_keys('anusreemanu')
log_button=driver.find_element_by_xpath("//button[@type='submit']")
log_button.click()
search=driver.find_element_by_xpath("//input[@type='search']")
search.send_keys("Sherin Mariyamma")
search.send_keys(Keys.ENTER)

#print(driver.title)
extitle='Log in to Facebook'
ct=driver.title
if extitle==ct:
    print('Tested successfully')
else:
    print('Testing failed')