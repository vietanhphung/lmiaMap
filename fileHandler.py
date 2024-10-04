import pandas as pd
import requests
import io
def handleExcel(path):
    r = requests.get(path, stream=True)
    with io.BytesIO(r.content) as fh:
        df = pd.io.excel.read_excel(fh, sheet_name=0)
    return df.tolist()













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
