import json
import requests
import csv
import pandas as pd


url ="https://open.canada.ca/data/api/action/package_show?id=f82f66f2-a22b-4511-bccf-e1d74db39ae5"
provinces = {
    "Alberta",
    "British Columbia",
    "Manitoba",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Nova Scotia",
    "Ontario",
    "Prince Edward Island",
    "Quebec",
    "Saskatchewan"
    "Northwest Territories",
    "Nunavut",
    "Yukon"
}

transformed_data = []
province = ''
language = '_'+'en'
response = requests.get(url)
data = response.json()


# data for year 2024, need to handle different formats of csv files
#for j in range(len(data["result"]["resources"])-1,-1):
for j in range(len(data["result"]["resources"])-1,len(data["result"]["resources"])-12,-1):
    url2 = (data["result"]["resources"][j]["url"])


    if language in url2:
        csvFile = requests.get(url2)
        try:
            decoded_content = csvFile.content.decode()
        except:
            decoded_content = csvFile.content.decode('latin-1')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        data_list = list(cr)[1:]
        filtered_rows = [row for row in data_list if row != [] and row != ['Employer ', 'Address', 'Positions Requested']]

        year = data["result"]["resources"][j]["name"][:4]
        for i in range(len(filtered_rows)-3):
            if filtered_rows[i][0] in provinces:
                province = filtered_rows[i][0]
            else:
                filtered_rows[i].append(province)
                filtered_rows[i].append(year)
                transformed_data.append(filtered_rows[i] )
        print(j,year)


with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(transformed_data)
