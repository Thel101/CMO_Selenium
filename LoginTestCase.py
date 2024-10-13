from selenium import webdriver
from selenium.webdriver.chrome.service import Service #selenium 4 standard
from selenium.webdriver.common.by import By

ser_obj = Service() #selenium 4 standard
driver = webdriver.Chrome(service=ser_obj)
#driver is an object of Chrome class

driver.get("https://opensource-demo.orangehrmlive.com/")


driver.implicitly_wait(5)
driver.find_element(By.NAME, 'username').send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
actual_title = driver.title
expected_title = 'OrangeHRM'
if actual_title == expected_title:
    print("Login Successful")
else:
    print("Login Failed")

# driver.find_element(By.NAME, "username").send_keys("Admin")

# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# actual_title = driver.title
# expected_title = 'OrangeHRM'
# if actual_title == expected_title:
#     print("Login Successful")
# else:
#     print("Login Failed")