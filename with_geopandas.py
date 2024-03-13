import geopandas as gpd
import matplotlib.pyplot as plt

# Load ZIP code boundaries data for the USA
# zip_codes_usa = gpd.read_file("https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_zcta510_500k.zip")

zip_codes_usa = gpd.read_file(r".\\cb_2018_us_zcta510_500k.zip")

def plot_zip_codes(zip_codes):
    # Plot ZIP code boundaries
    fig, ax = plt.subplots(figsize=(10, 10))
    zip_codes_usa.plot(ax=ax, color='lightgrey', edgecolor='black')

    for zip_code in zip_codes:
        zip_code_boundary = zip_codes_usa[zip_codes_usa["ZCTA5CE10"] == zip_code]

        # Plot ZIP code boundaries
        zip_code_boundary.plot(ax=ax, color='red', alpha=0.5)

        # Plot the center of the ZIP code
        centroid = zip_code_boundary.geometry.centroid
        plt.scatter(centroid.x, centroid.y, color='blue', label=f'ZIP Code {zip_code} Center')

    # Add labels and legend
    plt.title("ZIP Code Boundaries")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()

    # Adjust axis limits
    ax.set_xlim(zip_codes_usa.total_bounds[0], zip_codes_usa.total_bounds[2])
    ax.set_ylim(zip_codes_usa.total_bounds[1], zip_codes_usa.total_bounds[3])
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_box_aspect(0.5)
    ax.autoscale()


    return fig

zip_codes = ['30301','02101','60601','75201','77001','90001','33101','10001','19101','85001','94101','98101','20001']
map_with_zip_codes = plot_zip_codes(zip_codes)

# Save the plot as an HTML file
map_with_zip_codes.savefig('with_geopandas_map.html', format='html')

print("Map saved as with_geopandas_map.html.")
