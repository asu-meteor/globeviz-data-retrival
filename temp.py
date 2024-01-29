import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset

# Load your NetCDF file
nc_file_path = 'files/single_files/SSTF/2022/353/16/OR_ABI-L2-SSTF-M6_G18_s20223531600212_e20223531659520_c20223531705430.nc'
# nc_file_path = 'files/single_files/LSTF/2023/069/07/OR_ABI-L2-LSTF-M6_G18_s20230690700208_e20230690709516_c20230690711253.nc'
dataset = Dataset(nc_file_path)

latlon_path = 'goes16_abi_full_disk_lat_lon.nc'
lat_lons = Dataset(latlon_path)

lats = lat_lons.variables['latitude'][:]
lons = lat_lons.variables['longitude'][:]
variable = dataset.variables['SST'][:]

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