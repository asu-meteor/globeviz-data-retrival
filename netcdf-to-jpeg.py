import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import pandas as pd

# Load your NetCDF file
# nc_file_path = 'files/single_files/SSTF/2022/353/16/OR_ABI-L2-SSTF-M6_G18_s20223531600212_e20223531659520_c20223531705430.nc'
nc_file_path = '/Users/yashshah/Downloads/OR_ABI-L2-TPWF-M6_G16_s20240010000205_e20240010009513_c20240010011108.nc'
dataset = Dataset(nc_file_path)

# lat_lon_file_path = 'goes16_abi_full_disk_lat_lon.nc'
# lat_lons = Dataset(lat_lon_file_path)

# for key in lat_lons.variables.keys():
#     print(key)

def calculate_degrees(file_id):

    np.seterr(all='ignore')
    
    # Read in GOES ABI fixed grid projection variables and constants
    x_coordinate_1d = file_id.variables['x'][:]  # E/W scanning angle in radians
    y_coordinate_1d = file_id.variables['y'][:]  # N/S elevation angle in radians
    projection_info = file_id.variables['goes_imager_projection']
    lon_origin = projection_info.longitude_of_projection_origin
    H = projection_info.perspective_point_height+projection_info.semi_major_axis
    r_eq = projection_info.semi_major_axis
    r_pol = projection_info.semi_minor_axis

    """
    - Chunk the data into matrix and work for conversion
    - Then combine the chunks
    - Figure how to merge them back together
    - Explore 3D Tiling
    - Use offshelf tool
    - Explore Python options for chunking

    """
    
    # Create 2D coordinate matrices from 1D coordinate vectors
    x_coordinate_2d, y_coordinate_2d = np.meshgrid(x_coordinate_1d, y_coordinate_1d)
    
    # Equations to calculate latitude and longitude
    lambda_0 = (lon_origin*np.pi)/180.0  
    a_var = np.power(np.sin(x_coordinate_2d),2.0) + (np.power(np.cos(x_coordinate_2d),2.0)*(np.power(np.cos(y_coordinate_2d),2.0)+(((r_eq*r_eq)/(r_pol*r_pol))*np.power(np.sin(y_coordinate_2d),2.0))))
    b_var = -2.0*H*np.cos(x_coordinate_2d)*np.cos(y_coordinate_2d)
    # print(b_var)
    c_var = (H**2.0)-(r_eq**2.0)
    r_s = (-1.0*b_var - np.sqrt((b_var**2)-(4.0*a_var*c_var)))/(2.0*a_var)
    s_x = r_s*np.cos(x_coordinate_2d)*np.cos(y_coordinate_2d)
    s_y = - r_s*np.sin(x_coordinate_2d)
    s_z = r_s*np.cos(x_coordinate_2d)*np.sin(y_coordinate_2d)
    
    # Ignore numpy errors for sqrt of negative number; occurs for GOES-16 ABI CONUS sector data
    
    
    abi_lat = (180.0/np.pi)*(np.arctan(((r_eq*r_eq)/(r_pol*r_pol))*((s_z/np.sqrt(((H-s_x)*(H-s_x))+(s_y*s_y))))))
    abi_lon = (lambda_0 - np.arctan(s_y/(H-s_x)))*(180.0/np.pi)

    # abi_lat = np.where(np.isnan(abi_lat), 0, abi_lat)
    # abi_lon = np.where(np.isnan(abi_lon), 0, abi_lon)
    return abi_lat, abi_lon

lats, lons = calculate_degrees(dataset)
# print(lats.shape, lons.shape)
# Extract the necessary variables
# lat = lat_lons.variables['latitude'][:]
# lon = lat_lons.variables['longitude'][:]
lat = lats
lon = lons
variable = dataset.variables['TPW'][:]
fill_value = 0
variable = np.where(variable == None, fill_value, variable)
# variable = np.where(variable == None, 0, variable)

# Create a meshgrid for lon and lat
# lon, lat = np.meshgrid(lon, lat)

# Create a figure and axis using Basemap
fig, ax = plt.subplots(figsize=(10, 6))
m = Basemap(projection='cyl', resolution='i')

# Plot the data on the map as color contours
x, y = m(lons, lats)
contour_plot = m.contourf(x, y, variable, cmap='viridis', levels=20)

# Add coastlines and other map features
m.drawcoastlines()
m.drawcountries()

# Add a colorbar
cbar = plt.colorbar(contour_plot, ax=ax, orientation='vertical', pad=0.1)
cbar.set_label('Your Variable Unit')

# Set plot title
plt.title('')

# Show the plot
plt.show()
