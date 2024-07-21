from bs4 import BeautifulSoup
import requests
import pandas

url = "https://shs.osu.edu/about-us/provider-directory"

response = requests.get(url)

if response.status_code == 200:
    print("Works!")
else :
    print("DaGabagoo")
    
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

#print(soup)

name_tags = soup.find_all("h2", class_="c-card__header")

firstName = []
lastName = []

for name_tag in name_tags :
    full_name_and_title = name_tag.contents[0].strip()
    full_name = full_name_and_title.split(", ")[0]
    firstName.append(full_name.split(" ")[0])
    lastName.append(full_name.split(" ")[1])


csv_file = "osu.csv"

Names = {"First Name" : firstName, "Last Name" : lastName}

df = pandas.DataFrame(Names)

df.to_csv("osu.csv", index = False)
