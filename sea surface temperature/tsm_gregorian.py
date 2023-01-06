from netCDF4 import Dataset
from function import filename2
import datetime as dt

#Arquivo que faz as medias de maneira manual
arquivo = 'outfile.nc'
nc_f = arquivo

#To show the file variables
nc_fid = Dataset(arquivo, 'r')  # Dataset is the class behavior to open the file
                             # and create an instance of the ncCDF4 class
#nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)
lats, lons, time, lev = filename2(nc_f)

dt_time = [dt.date(1891, 1, 1) + dt.timedelta(hours=t)
           for t in time]

print(dt_time)
