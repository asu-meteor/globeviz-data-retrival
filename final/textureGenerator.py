import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

def textureGenerator(file, name, lats, lons, variable):
    dataset = Dataset(file)
    fig, ax = plt.subplots(figsize=(10, 6))
    m = Basemap(projection='cyl', resolution='f')
    data = dataset.variables['{variable}'.format(variable=variable)][:]
    # Plot the data on the map as color contours
    x, y = m(lons, lats)
    contour_plot = m.contourf(x, y, data, cmap='viridis')

    # Add coastlines and other map features
    m.drawcoastlines()
    m.drawcountries()

    # Add a colorbar
    # cbar = plt.colorbar(contour_plot, ax=ax, orientation='vertical', pad=0.1)
    # cbar.set_label('Your Variable Unit')

    # Set plot title
    plt.title('')
    plt.savefig('{name}.png'.format(name=name), bbox_inches='tight', pad_inches=-0.05)
    # plt.savefig('output_plot.png', format='png', dpi=300, bbox_inches=(0.1, 0.1, 0.9, 0.9))
    # Show the plot
    plt.show()