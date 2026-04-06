from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.minimize_window()

driver.get(" https://practicetestautomation.com/practice-test-login/")

time.sleep(3)

username = driver.find_element(By.ID,"username")
username.send_keys("student")
password = driver.find_element(By.ID, "password")
password.send_keys("Password123")
time.sleep(3)
login = driver.find_element(By.ID , "submit")
login.click()
succuss_text = driver.find_element(By.CLASS_NAME , "post-title").text

if "Logged In Successfully" in succuss_text:
        print("Test Passed: Login successful!")
else:
    print("Test Failed: Login text not found.")
time.sleep(3)
driver.quit() 