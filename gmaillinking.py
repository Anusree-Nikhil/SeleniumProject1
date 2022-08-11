from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.google.com/")
from selenium.webdriver.common.by import By

link=driver.find_element_by_link_text("Gmail")
link.click()
sign_button=driver.find_element_by_link_text("Sign in")
sign_button.click()
mail=driver.find_element(by=By.ID,value="identifierId")
mail.send_keys("anusree265@gmail.com")
next_button=driver.find_element_by_id("identifierNext")
next_button.click()
"""password=driver.find_element(by=By.NAME,value="password")
password.send_keys("")
check_box=driver.find_element(by=By.NAME,value='Show password')
check_box.click()
next2_button=driver.find_element_by_id("passwordNext")
next2_button.click()"""

print(driver.title)

et="Gmail"
ct=driver.title
if et==ct:
    print("Tested succesfully..")
else:
    print("Testing failed")

