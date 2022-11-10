from netCDF4 import Dataset 
import numpy as np

def filename2(fn):
	#nc_fid = Dataset('./2020files/%s'%(fn), 'r')  # Dataset is the class behavior to open the file
	nc_fid = Dataset(fn, 'r')
        #nc_fid = Dataset(fn, 'r')
                             # and create an instance of the ncCDF4 class
		#Print the descripsion of the data, optional. 
	#nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)

#The  above command shown that there are 4 variables
#in the nc_f = ./air.sig995.2012.nc file.  
#The data shown the air temperature of 1 year. 
# Extract data from NetCDF file
	lats = nc_fid.variables['lat'][:]  # extract/copy the data
	lons = nc_fid.variables['lon'][:]
	time = nc_fid.variables['time'][:]
	precip  = nc_fid.variables['precip'][:]  # shape is time, lat, lon as shown above
	#print(precip)
	return lats, lons, precip, time







   


   

