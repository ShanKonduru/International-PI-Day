import folium

# Lookup table for latitude and longitude coordinates of ZIP codes
zip_code_coordinates = {
    '30301': (33.7490, -84.3880),
    '02101': (42.3601, -71.0589),
    '60601': (41.8855, -87.6226),
    '75201': (32.7876, -96.7983),
    '77001': (29.7604, -95.3698),
    '90001': (33.9738, -118.2484),
    '33101': (25.7743, -80.1937),
    '10001': (40.7506, -73.9971),
    '19101': (39.9526, -75.1652),
    '85001': (33.4484, -112.0740),
    '94101': (37.7749, -122.4194),
    '98101': (47.6101, -122.3346),
    '20001': (38.9041, -77.0172)
}

# Function to plot ZIP codes on map using Folium
def plot_zip_codes(zip_codes):
    # Create a map centered on the US
    m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    # Add ZIP codes as markers
    for zip_code in zip_codes:
        lat, lon = zip_code_coordinates.get(zip_code, (None, None))
        if lat is not None and lon is not None:
            folium.Marker([lat, lon], icon=folium.Icon(icon='info-sign')).add_to(m)

    return m

# Example usage
zip_codes = ['30301','02101','60601','75201','77001','90001','33101','10001','19101','85001','94101','98101','20001']  # Example ZIP codes

map_with_zip_codes = plot_zip_codes(zip_codes)
map_with_zip_codes.save('map_with_zip_codes.html')
