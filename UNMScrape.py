import requests
import json
import pandas as pd


url = "https://hsc.unm.edu/directory/index.json"

response = requests.get(url)

#Checks if request was successful
if (response.status_code == 200) :
    print("Works!")
else :
    print("does not work")

#print(response.text)

jsonData = response.json()

first_name = []
last_name = []

for i in range (len(jsonData["faculty"])) :
    
    if "SOM - Anesthesiology" in (jsonData["faculty"][i]["departments"]) :
        #print(jsonData["faculty"][i]["firstName"] + " " + jsonData["faculty"][i]["lastName"])
        first_name.append(jsonData["faculty"][i]["firstName"])
        last_name.append(jsonData["faculty"][i]["lastName"])
        
data = {'First Name':first_name, 'Last Name': last_name}

df = pd.DataFrame(data)

csv_file='unm.csv'
df.to_csv(csv_file, index = True)
