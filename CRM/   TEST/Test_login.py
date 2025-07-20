from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://cisco.odoo.com/web/login")
time.sleep(2)

email_field = driver.find_element(By.NAME, "login")
email_field.send_keys("manishguptacpj34@gmail.com")
time.sleep(2)

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Gupta@#12345")
time.sleep(2)

password_field.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "o_app")))
time.sleep(2)

crm_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.//div[contains(text(),'CRM')]]")))
crm_icon.click()
time.sleep(4)

new_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='New']")))
new_button.click()
time.sleep(2)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'o_kanban_quick_create')]")))
time.sleep(2)

company = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Company')]")
company.click()
company.clear()
# company.send_keys("cisco.ai")
time.sleep(2)

contact = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Contact')]")
contact.clear()
# contact.send_keys("9110298887")
time.sleep(2)


opp_name = driver.find_element(By.XPATH, "//input[contains(@placeholder, \"Opportunity\")]")
opp_name.click()
opp_name.clear()
opp_name.send_keys("sales")
time.sleep(2)

email = driver.find_element(By.XPATH, "//input[@type='email']")
email.send_keys("manishguptacpj34@gmail.com")
time.sleep(2)

phone = driver.find_element(By.XPATH, "//input[@type='tel']")
phone.send_keys("91101298887")
time.sleep(2)

amount = driver.find_element(By.XPATH, "//input[contains(@class, 'o_field_float')]")
amount.clear()
amount.send_keys("100000")
time.sleep(2)

add_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
add_button.click()
time.sleep(3)

time.sleep(10)
driver.quit()