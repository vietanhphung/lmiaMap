import pandas as pd
import requests
import certifi
import os
import geocode

provinces = {'newbrunswick', 'newfoundlandandlabrador', 'yukon', 'manitoba', 'northwestterritories', 'nunavut', 'alberta', 'nova scotia', 'saskatchewan', 'britishcolumbia', 'quebec', 'princeedwardisland', 'ontario'}


def handleExcel(path, year):
    
    os.environ['SSL_CERT_FILE'] = certifi.where()
    data = pd.read_excel(path, header=None)
    print('Accessing ' + str(year) + ' excel file')
    data.insert(0,'year',year)
    filtered_data = data[data[data.columns[-1]].notna() & (data[data.columns[-1]] != '') &(data[data.columns[1]] != 'Province/Territory')  ]
    return filtered_data









##################################
def xxxxxxx():
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
