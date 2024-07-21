from bs4 import BeautifulSoup
import requests
import re
import pandas

url = "https://www.upstate.edu/anesthesiology/about-us/faculty.php"

response = requests.get(url)

if response.status_code == 200 :
    print("Works!")
else :
    print("Not works")
    
pattern = re.compile(r'\?empID=')

soup = BeautifulSoup(response.text, "html.parser")

names = soup.find_all("a", href=pattern)
firstName = []
lastName = []
    
for name in names :
    full_name_and_title = name.contents[0].strip()
    full_name = full_name_and_title.split(", ")[0]
    firstName.append(full_name.split(" ")[0])
    if(len(full_name.split(" "))>2):
        lastName.append(full_name.split(" ")[len(full_name.split(" "))-1])
        
    else:
        lastName.append(full_name.split(" ")[1])

print(firstName)
print(lastName)


csv_file = "umu.csv"

Names = {"First Name" : firstName, "Last Name" : lastName}

df = pandas.DataFrame(Names)

df.to_csv(csv_file, index = False)
