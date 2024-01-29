import os 
# from osgeo import gdal
import subprocess
import numpy as np
from PIL import Image

bucket_name = "s3://noaa-goes18"



# result = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L1b-RadC/2023/001/00/", shell=True, check=True, stdout=subprocess.PIPE, text=True)
# file_list_output = result.stdout
# file_list = file_list_output.strip().split('\n')

# print(file_list[0].split()[3])
# command = "aws s3 cp --no-sign-request s3://noaa-goes18/ABI-L1b-RadC/2023/001/00/{file_name} files/{file_name}".format(file_name = file_list[0].split()[3])

# subprocess.run(command, shell=True, check=True)

def LSTF_main():
    result = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-LSTM/", shell=True, check=True, stdout=subprocess.PIPE, text=True)
    years_list = result.stdout
    years = years_list.strip().split('\n')
    years = [x.split()[-1] for x in years]
    print(years)
    for year in years:
        print("Running for year: ", year)
        res = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-LSTM/{year}".format(year=year), shell=True, check=True, stdout=subprocess.PIPE, text=True)
        days_list = res.stdout
        days = days_list.strip().split('\n')
        days = [x.split()[-1] for x in days]
        print(days)
        for day in days:
            print("Running for day: ", day)
            temp_res = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-LSTM/{year}{day}".format(year=year, day=day), shell=True, check=True, stdout=subprocess.PIPE, text=True)
            hours_list = temp_res.stdout
            hours = hours_list.strip().split('\n')
            hours = [x.split()[-1] for x in hours]
            print(hours)
            for hour in hours:
                print("Running for hour: ", hour)
                temp_res1 = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-LSTM/{year}{day}{hour}".format(year=year, day=day, hour=hour), shell=True, check=True, stdout=subprocess.PIPE, text=True)
                files_list = temp_res1.stdout
                files = files_list.strip().split('\n')
                files = [x.split()[-1] for x in files]
                print(files)
                for file in files:
                    print("Downloading file: ", file)
                    subprocess.run("aws s3 cp --no-sign-request s3://noaa-goes18/ABI-L2-LSTM/{year}{day}{hour}{file_name} files/LSTM/{year}{day}{hour}{file_name}".format(year=year, day=day, hour=hour, file_name=file), shell=True, check=True)
# RadC_main()


def LSTF_single():
    year = input("Please enter year: ")
    day = input("Please enter day: ")
    hour = input("Please enter hour: ")
    temp_res = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-LSTF/{year}/{day}/{hour}/".format(year=year, day=day, hour=hour), shell=True, check=True, stdout=subprocess.PIPE, text=True)
    files_list = temp_res.stdout
    files = files_list.strip().split('\n')
    files = [x.split()[-1] for x in files]
    # print(files)
    # file = files[0]
    for file in files:

    # print(file)
        subprocess.run("aws s3 cp --no-sign-request s3://noaa-goes18/ABI-L2-LSTF/{year}/{day}/{hour}/{file} files/single_files/LSTF/{year}/{day}/{hour}/{file}".format(year=year, day=day, hour=hour, file=file), shell=True, check=True)

LSTF_single()

# netcdriver = gdal.GetDriverByName("netCDF")
# print(netcdriver)
# print(os.getcwd())
# nc_file_path = "files/2022/169/17/OR_ABI-L1b-RadC-M6C10_G18_s20221691716171_e20221691718555_c20221691718587.nc"

# dataset = gdal.Open(nc_file_path, gdal.GA_ReadOnly)
# variable = dataset.GetRasterBand(1).ReadAsArray()