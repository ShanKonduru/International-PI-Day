import folium
import pandas as pd
from opencage.geocoder import OpenCageGeocode

# OpenCage API key
api_key = '5239cc6950284dc9b776bcd44b54bd77'

# Function to get latitude and longitude of a ZIP code
def get_coordinates(zip_code):
    geocoder = OpenCageGeocode(api_key)
    query = f'{zip_code}, USA'
    results = geocoder.geocode(query)
    if results and len(results):
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        print(f"Could not find coordinates for ZIP code {zip_code}")
        return None, None

# Function to plot ZIP codes on map using Folium
def plot_zip_codes(zip_codes):
    # Create a map centered on the US
    m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    # Add ZIP codes as markers
    for zip_code in zip_codes:
        lat, lon = get_coordinates(zip_code)
        if lat is not None and lon is not None:
            folium.Marker([lat, lon], icon=folium.Icon(icon='info-sign')).add_to(m)

    return m

# Example usage
zip_codes = ['30301','02101','60601','75201','77001','90001','33101','10001','19101','85001','94101','98101','20001']  # Example ZIP codes

map_with_zip_codes = plot_zip_codes(zip_codes)
map_with_zip_codes.save('opencage_map_with_zip_codes.html')
