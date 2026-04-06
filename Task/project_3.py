
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(2)
search = driver.find_element(By.ID, "APjFqb")
search.click()

search.send_keys("Python Selenium tutorial")
search.send_keys(Keys.RETURN)

# title = driver.find_elements(By.XPATH, "//div[@class='MjjYud']//h3")

title = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='MjjYud']//h3"))
    )

for t in title:
    print(t.text)

        

time.sleep(3)
driver.quit()