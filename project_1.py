from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

driver.get("http://quotes.toscrape.com")

time.sleep(2)

quote = driver.find_elements(By.XPATH, "//span[@class='text']")
author = driver.find_elements(By.XPATH, "//small[@class='author']")

data = []

for i in range(len(quote)):
    quote_text = quote[i].text
    author_name = author[i].text
    data.append(["Quote " " ", quote_text])
    data.append(["Author" " ", author_name])
    data.append([])

driver.quit()


with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

