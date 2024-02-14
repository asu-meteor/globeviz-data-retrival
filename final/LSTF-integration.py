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
    temp_res = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-LSTF/{year}/{day}/{hour}/".format(year=year, day=day, hour=hour), shell=True, check=True, stdout=subprocess.PIPE, text=True)
    files_list = temp_res.stdout
    files = files_list.strip().split('\n')
    