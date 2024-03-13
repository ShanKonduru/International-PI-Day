import folium
from geopy.geocoders import Nominatim

def get_lat_long(zip_code):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(zip_code + ", USA")
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Example usage:
zip_code = "30301"  # Enter your ZIP code here
lat_long = get_lat_long(zip_code)
if lat_long:
    # Create a map centered around the provided ZIP code
    m = folium.Map(location=lat_long, zoom_start=10)
    
    # Add a marker for the provided location
    folium.Marker(location=lat_long, popup=zip_code).add_to(m)
    
    # Save the map to an HTML file
    m.save("with_geopy.html")
    print("Map saved as map.html.")
else:
    print("No location found for the provided ZIP code.")
