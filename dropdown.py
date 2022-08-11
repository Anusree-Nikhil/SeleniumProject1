from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.orangehrm.com/open-source/demo/")
driver.maximize_window()
driver.implicitly_wait(10)

"""select=driver.find_element(by=By.XPATH,value="//select[@id='Form_submitRequest_Country']")
select_dd=Select(select)
#select_dd.select_by_value("India")
#select_dd.select_by_index(12)
select_dd.select_by_visible_text("India")
#driver.quit()
"""
#OR

select=driver.find_element(by=By.XPATH,value="//select[@id='Form_submitRequest_Country']")
select_dd=Select(select)
allcountries=select_dd.options
for c in allcountries:
    if c.text=="India":
        c.click()