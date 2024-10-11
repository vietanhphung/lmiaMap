import pandas as pd
import googlemaps

# Initialize the Google Maps client with your API key
API_KEY = 'YOUR_GOOGLE_API_KEY'
gmaps = googlemaps.Client(key=API_KEY)

# Example DataFrame with an Address column
data = {'Address': ['1600 Amphitheatre Parkway, Mountain View, CA',
                    '1 Apple Park Way, Cupertino, CA']}
df = pd.DataFrame(data)

# Function to get latitude and longitude from Google Maps Geocoding API
def get_coordinates_from_gmaps(address):
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location['lat'], location['lng']
    except Exception as e:
        print(f"Error geocoding {address}: {e}")
    return None, None

# Apply the function to the DataFrame column
df['Latitude'], df['Longitude'] = zip(*df['Address'].apply(get_coordinates_from_gmaps))

# Display the DataFrame with coordinates
print(df)
