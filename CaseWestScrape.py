from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas
import time

service = Service('/Users/adityapandey/Downloads/chromedriver-mac-x64/chromedriver')

driver = webdriver.Chrome(service=service)

driver.get("https://bulletin.case.edu/medicine/faculty/#fulltimefacultytext")

time.sleep(5)

Anesthesiology_button = driver.find_element(By.LINK_TEXT, "Anesthesiology")
Anesthesiology_button.click()

time.sleep(1)

faculty_names = driver.find_elements(By.CSS_SELECTOR, "p")
print(faculty_names)
