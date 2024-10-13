import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("")
driver = webdriver.Chrome()

driver.get("https://shop.preprod.citymall.com.mm/")
driver.maximize_window()
mywait = WebDriverWait(driver, 10)
#given argument as tuple
language = mywait.until(EC.presence_of_element_located((By.XPATH,"//form[@id='desktop-lang-form']//span[@class='hidden-xs'][normalize-space()='my']")))
language.click()

en_language = mywait.until(EC.presence_of_element_located((By.XPATH,"//form[@id='desktop-lang-form']//li[@class='lang-selector'][normalize-space()='en']")))
en_language.click()

login = mywait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='/citymall/en/login']")))
login.click()

login_option = mywait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='login_type']")))
login_option.click()

mobile_login = mywait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login_type']/option[1]")))
mobile_login.click()

phone_field = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='j_username1']")))
phone_field.send_keys("9783979898")

password_field = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='j_password']")))
password_field.send_keys("Def@u1tPW")

login_btn = mywait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Log In']")))
login_btn.click()

product = mywait.until(EC.presence_of_element_located((By.LINK_TEXT ,'Ok Happy Rose Facial Tissue 3Ply 3X420 Sheets')))
product.click()

increase_qty = mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='+']")))
increase_qty.click()

add_to_cart_btn = mywait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='ADD TO CART']")))
add_to_cart_btn.click()

cart = mywait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[3]/a")))
cart.click()


checkout_btn = mywait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Proceed To Checkout']")))
checkout_btn.click()

mywait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='addressSubmit']"))).click()
mywait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='standard-week-42-day-0-slot']/div[1]"))).click()
mywait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='deliveryMethodSubmit']"))).click()
mywait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='confirmToPayment']"))).click()
mywait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='confirmPopup']")))
mywait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div[5]/div[3]/div[1]/div[1]/div[2]/div/div[4]/div/div[6]/div/div/div[2]/form/div[2]/div[2]/button"))).click()

mywait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='payment-pane']/div[5]/div/div/label/text()[1]"))).click()
# mywait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cboxClose']"))).click()
print('success')
mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Pay and confirm order')]"))).click()


print('success')