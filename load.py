import mysql.connector
import pandas as pd
from dotenv import dotenv_values
import pathlib

# Define paths for configuration and script
configuration_path = pathlib.Path(__file__).parent.resolve()
script_path = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(f"{configuration_path}/variables.conf")

# Load database credentials from .env file
password = config["db_password"]
user = config["dbuser"]
db = config["dbname"]
tb = config["tbname"]
print(tb)

# Database connection parameters
db_config = {
    'host': '127.0.0.1',
    'user': user,
    'password': password,
    'database': db
}

# CSV file path
csv_file_path = 'data.csv'

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Load data from CSV
df = pd.read_csv(csv_file_path)


insert_query = f"""
    INSERT INTO {tb} (year, province, stream, employer, address, occupation, incorporate_status, requested_lmia, requested)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
print(insert_query)

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
        row['requested']          
    ))

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")
