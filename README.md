# globeviz-data-retrival
## Overview
This is the repository for the Dreamscape DataViz team, specifically working on 
the project of Globe Visualization. The code contained in this repo relates to the 
task of downloading the data from the AWS servers, processing the data in netCDF 
format, and then creating the textures that can be wrapped around the 3D Globe in
Unity. 

## Prerequisites
Following are the prerequisites that are required to run the code successfully, and 
are needed in the environment to successfully execute the scripts. 

- AWSCLIv2 package: The scripts used to download the data from the AWS S3 buckets uses unsigned AWSCLI request to make the request to download and browse the buckets. 
- For processing the data downloaded, we need the use the netCDF4 package, which enables efficient multithreadded processing of large netCDF datasets, and allows us to work and combine multiple 
netCDF files. 
- For goes-imager-projection conversion, we need to use NumPy, to carry out the complex
calculations used for the conversion. 
- Lastly, for generating the texture image, matplotlib, PyPlot and BaseMap is used. 

## Detailed Functionality
Following are the detailed steps on how the whole process works: 

- First of all, upon receiving the input from the user, the script to download the
appropriate dataset is triggered, which downloads the data, and puts the data in respective folder. 
- Then, once the data is downloaded, next step of converting goes-imager-projection to normal
lats-lons is triggered, and depending if the data downloaded was CONUS (Continental US), or 
Full Disk (Encompasses whole globe), this can take varying amount of time. 
- After the conversion of the dataset, the texture creation step loads the data, and 
then loads the basemap, then plots the data in resolution agreed upon. Full resolution, 
while being the highest quality of resolution, takes the longest time to render. 

## Future Improvement
- Integrating the scripts into Unity, so can be triggered from headset. 
- Creating unified script, triggering all the step functions automatically. 

## Support
For any questions or doubts, please reach out to @yshah34 or yshah34@asu.edu. 

## Authors
- Yash Dilipkumar Shah
- Neha Balamurugan
- Dr. Robert LiKamWa