from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "C:\Program Files\selenium_chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
cookie = driver.find_element(By.ID, "bigCookie")
clicks = 500
while clicks != 0:
    for i in range(clicks):
        cookie.click()
    end = False
    while not end:
        time.sleep(0.1)
        upgrades = driver.find_elements(By.CSS_SELECTOR, "div#wrapper div#game div#sectionRight div#store div#upgrades div.enabled")
        if len(upgrades) != 0:
            upgrades[len(upgrades)-1].click()
        else:
            products = driver.find_elements(By.CSS_SELECTOR, "div#wrapper div#game div#sectionRight div.enabled")
            if len(products) != 0:
                products[len(products)-1].click()
            else:
                end = True
    # count = driver.find_element(By.CSS_SELECTOR, "div#wrapper div#game div#sectionLeft div#cookies").text
    # print(int(count.split()[0]))
# try:
#     cookie = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "bigCookie")))
#     print("Success")
# except TimeoutError:
#     print("TimeOut")
#     driver.close()
