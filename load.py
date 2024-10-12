import mysql.connector
import pandas as pd
from db_con import db_connect


# Load data from CSV
csv_file_path = 'data.csv'
df = pd.read_csv(csv_file_path)

# Connect to the database
db_config = db_connect()
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

tb='lmia_tb'


insert_query = f"""
    INSERT INTO {tb} (year, province, stream, employer, address, occupation, incorporate_status, requested_lmia, requested, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """


# Insert data into the table
for index, row in df.iterrows():

    cursor.execute(insert_query, (
        row['year'],              
        row['province'],          
        row['stream'],            
        row['employer'],          
        row['address'],          
        row['occupation'],       
        row['incorporate_status'],
        row['requested_lmia'],    
        row['requested'],
        row['latitude'],
        row['longitude']          
    ))

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")
