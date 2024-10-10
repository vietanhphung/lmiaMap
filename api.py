import requests
from fileHandler import *
import pandas as pd

url ="https://open.canada.ca/data/api/action/package_show?id=f82f66f2-a22b-4511-bccf-e1d74db39ae5"


dt = pd.DataFrame()
province = ''
language = '_'+'en'
response = requests.get(url)
r = response.json()


# data for year 2024, need to handle different formats of csv files
#for j in range(len(r["result"]["resources"])-1,-1):
for j in range(len(r["result"]["resources"])-1,len(r["result"]["resources"])-12,-1):
    url2 = (r["result"]["resources"][j]["url"])
    year = r["result"]["resources"][j]["name"][:4]
    
    if language in url2: #language = en
        
        fType = url2.split('.')[-1] #find file type to call appropriate handler
        if fType == 'xlsx': #match file type to correct handler
            data =  handleExcel(url2 , year)
            dt = pd.concat([dt, data], ignore_index=True)
            print(str(year) + ' data updated')
  
dt.columns = ['year', 'province', 'stream', 'employer', 'address', 'occupation', 'incorporate_status', 'requested_lmia', 'requested']


dt.to_csv('data.csv', index=False)
print("All data saved to csv file")



