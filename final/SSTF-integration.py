import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import pandas as pd
import subprocess
from goesConverter import calculate_degrees
from textureGenerator import textureGenerator

def main():
    year = input("Please enter year: ")
    day = input("Please enter day: ")
    hour = input("Please enter hour: ")
    temp_res = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-SSTF/{year}/{day}/{hour}/".format(year=year, day=day, hour=hour), shell=True, check=True, stdout=subprocess.PIPE, text=True)
    files_list = temp_res.stdout
    files = files_list.strip().split('\n')
    files = [x.split()[-1] for x in files]
    # print(files)
    file = files[0]
    # print(file)
    subprocess.run("aws s3 cp --no-sign-request s3://noaa-goes18/ABI-L2-SSTF/{year}/{day}/{hour}/{file} files/single_files/SSTF/{year}/{day}/{hour}/{file}".format(year=year, day=day, hour=hour, file=file), shell=True, check=True)

    lats, lons = calculate_degrees("files/single_files/SSTF/{year}/{day}/{hour}/{file}".format(year=year, day=day, hour=hour, file=file))

    lats, lons = np.array(lats), np.array(lons)

    textureGenerator("files/single_files/SSTF/{year}/{day}/{hour}/{file}".format(year=year, day=day, hour=hour, file=file), "SSTF_{year}_{day}_{hour}_{file}".format(year=year, day=day, hour=hour, file=file), lats, lons, "SST")

main()