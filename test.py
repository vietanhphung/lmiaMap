import requests
from fileHandler import *
import csv


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

dataToSave = []
province = ''
language = '_'+'en'
response = requests.get(url)
r = response.json()


# data for year 2024, need to handle different formats of csv files
#for j in range(len(r["result"]["resources"])-1,-1):
for j in range(len(r["result"]["resources"])-1,len(r["result"]["resources"])-12,-1):
    url2 = (r["result"]["resources"][j]["url"])
    if language in url2: #language = en
        fType = url2.split('.')[-1] #find file type
        match fType: #match file type to correct handler
            case 'xlsx':
                data =handleExcel(url2)
                print(data)
                dataToSave + data


       
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dataToSave)
