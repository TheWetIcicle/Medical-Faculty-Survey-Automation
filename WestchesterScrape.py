from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas


service = Service('/Users/adityapandey/Downloads/chromedriver-mac-x64/chromedriver')

driver = webdriver.Chrome(service=service)

driver.get('https://www.westchestermedicalcenter.org/anesthesiology-residency-program')

time.sleep(5)

faculty_button = driver.find_element(By.LINK_TEXT, 'Faculty')
faculty_button.click()

time.sleep(5)

faculty_names_elements = driver.find_elements(By.CSS_SELECTOR, 'p > span > strong')
print(type(faculty_names_elements[0]))
faculty_names = [element.text for element in faculty_names_elements]
filtered_faculty_names = [name for name in faculty_names if name != '']

firstName = []
lastName = []
    
for name in filtered_faculty_names :
    full_name_and_title = name.strip()
    full_name = full_name_and_title.split(", ")[0]
    firstName.append(full_name.split(" ")[0])
    if(len(full_name.split(" "))>2):
        lastName.append(full_name.split(" ")[len(full_name.split(" "))-1])
        
    else:
        lastName.append(full_name.split(" ")[1])

csv_file = "westchester.csv"

Names = {"First Name" : firstName, "Last Name" : lastName}

df = pandas.DataFrame(Names)

df.to_csv(csv_file, index = False)


# Step 5: Close the browser
driver.quit()

