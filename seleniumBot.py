from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://example.com/")

element = driver.find_element(By.LINK_TEXT, "More information...")
element.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/domains']")))
element.click()

time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 0);")

time.sleep(5)
driver.close()
