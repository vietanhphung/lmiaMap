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

def db_connect():
    return db_config