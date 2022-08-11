from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Anju Anil\\Desktop\\python\\chromedriver")
driver.get("https://www.rcvacademy.com/")

print(driver.title)
print(driver.current_url)
#driver.maximize_window()
driver.fullscreen_window()
driver.refresh()
driver.find_element_by_link_text("Register").click()

#driver.back()
#driver.forward()
#driver.minimize_window()

#driver.close()
#driver.quit()
