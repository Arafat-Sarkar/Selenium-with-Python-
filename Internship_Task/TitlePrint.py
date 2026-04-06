from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://selenium.dev")

print(browser.title)

browser.quit()