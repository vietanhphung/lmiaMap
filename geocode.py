import googlemaps
from dotenv import dotenv_values
import pathlib
import pandas as pd

# Define paths for configuration and script
configuration_path = pathlib.Path(__file__).parent.resolve()
script_path = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(f"{configuration_path}/apikey.conf")
googlekey = config["google"]
gmaps = googlemaps.Client(key=googlekey)

# Function to geocode a single address
def geocode(address):
    geocode_result = gmaps.geocode(address)
    location = geocode_result[0]['geometry']['location']
    return location['lat'], location['lng']

