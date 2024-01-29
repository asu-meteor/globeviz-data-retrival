# import os 
# from osgeo import gdal
# import subprocess
# import numpy as np
# from PIL import Image

# bucket_name = "s3://noaa-goes18"


# def SSTF_single():
#     year = input("Please enter year: ")
#     day = input("Please enter day: ")
#     hour = input("Please enter hour: ")
#     temp_res = subprocess.run("aws s3 ls --no-sign-request s3://noaa-goes18/ABI-L2-SSTF/{year}/{day}/{hour}/".format(year=year, day=day, hour=hour), shell=True, check=True, stdout=subprocess.PIPE, text=True)
#     files_list = temp_res.stdout
#     files = files_list.strip().split('\n')
#     files = [x.split()[-1] for x in files]
#     # print(files)
#     # file = files[0]
#     for file in files:

#     # print(file)
#         subprocess.run("aws s3 cp --no-sign-request s3://noaa-goes18/ABI-L2-SSTF/{year}/{day}/{hour}/{file} files/single_files/SSTF/{year}/{day}/{hour}/{file}".format(year=year, day=day, hour=hour, file=file), shell=True, check=True)

# SSTF_single()
import pyequilib
