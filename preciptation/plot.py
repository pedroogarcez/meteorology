
import numpy  as np 

import matplotlib as mpl

import matplotlib.pyplot as plt

#from  read_ncfiles import ncdump

#To import the library necessary to make the maps 

from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid


from matplotlib.colors import LinearSegmentedColormap

#colorpallet = LinearSegmentedColormap.from_list('mycmap', ['navy','gray','purple','white','green','yellow','red'], N=256, gamma=1.0)
#colorpallet = LinearSegmentedColormap.from_list('mycmap', ['navy','purple','gray','red','white','blue','yellow','green','red'], N=256, gamma=1.0)
colorpallet = LinearSegmentedColormap.from_list('mycmap', ['red','darkorange','orange','gold','yellow','white','lawngreen','green','teal','navy','blue'], N=256, gamma=1.0)
#cor mais forte ao redor do centro, para que haja maior contraste entre -2 e 2


    
def plot_precip(datatoplot,lats,lons,plotname,figname):

	#3)To plot the medium temperature in Autumm 2012.  ################################################################### #open figure 
    fig = plt.figure() #Adjust the location of the interior of the figgure fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9) # Setup the map. See http://matplotlib.org/basemap/users/mapsetup.html # for other projections.  #proj = ccrs.PlateCarree() 
	#proj = 'moll'
	
    #proj  = 'cyl'
    #proj  = 'moll'
    proj  = 'cyl'
    
    #Define latitudes to plot (-90,90)
    
    lat_i =   -90 
    lat_f =   90
    
    #Como o arquivo está disposto em coordenadas de -180 a 180, precisamos modificar nossa longitude. 
    #Define longitudes  to plot (-180,180)
    lon_i =  -180 
    lon_f =  180
    
    m = Basemap(projection=proj, llcrnrlat=lat_i, urcrnrlat=lat_f,\
                llcrnrlon=lon_i, urcrnrlon=lon_f, resolution='c', lon_0=0)

    
    #m = Basemap(projection='moll', llcrnrlat=-90, urcrnrlat=90,\
    #            llcrnrlon=0, urcrnrlon=360, resolution='c', lon_0=0)
    
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawcountries()
    m.drawparallels(np.arange(-60.,60.,30.),labels=[1,0,0,0]) # draw parallels
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1]) # draw meridians

    # Make the plot continuous
    #air_cyclic, lons_cyclic = addcyclic(datatoplot, lons[:])
    # Shift the grid so lons go from -180 to 180 instead of 0 to 360.
    
    #################
#    airchange, lonschange = shiftgrid(180., datatoplot, lons, start=False)
 #   exit()	
    # Create 2D lat/lon arrays for Basemapnc_f = './air.sig995.2012.nc'  # Your filename
#    lon2d, lat2d = np.meshgrid(lonschange, lats[:])
    lon2d, lat2d = np.meshgrid(lons, lats[:])
    # Transforms lat/lon into plotting coordinates for projection
    x, y = m(lon2d, lat2d)
    
    #numero de contornos
    # Plot of air temperature with 11 contour intervals
#    ncon = np.linspace(0, 350, 50, endpoint=True)
    ncon = np.arange(0,501,100)
#    cs = m.contourf(x, y, airchange, ncon, cmap=plt.cm.Spectral_r)
    #cs = m.contourf(x, y, datatoplot, ncon, cmap=plt.cm.Spectral_r)	
    cs = m.contourf(x, y, datatoplot, ncon, cmap='viridis')
    #cs = m.contourf(x, y, air_cyclic, 11, cmap='autumn', extend='both')

    cbar = plt.colorbar(cs,ticks=ncon[::1], orientation='horizontal', shrink=0.5)
#    cbar = plt.colorbar(cs, orientation='horizontal', shrink=0.5)
    #cbar.set_label("%s (%s)" % (nc_fid.variables['air'].var_desc,\
    #                            nc_fid.variables['air'].units))
    #plt.title("%s on %s" % (nc_fid.variables['air'].var_desc, cur_time))
    plt.title("%s"%(plotname))
    
    
   # plt.savefig('%s'%(figname), dpi=1000)
#    plt.savefig('%s.pdf'%(figname),bbox_inches='tight', format='pdf', dpi=1000)
    plt.savefig('%s'%(figname), dpi=1000)
#    plt.savefig(f'{figname}',dpi=1000)
    #media de cada estacao 
    #media anual 
    plt.show()
    return fig
   
def plot_anom(datatoplot,lats,lons,plotname,figname):
    colorpallet = LinearSegmentedColormap.from_list('mycmap',['blue','royalblue','olive','mediumaquamarine','palegreen','palegoldenrod','white','salmon','darkred','orange','orangered','yellow','red'], N=256,gamma=1.0)
	#3)To plot the medium temperature in Autumm 2012.  ################################################################### #open figure 
    fig = plt.figure() #Adjust the location of the interior of the figgure fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9) # Setup the map. See http://matplotlib.org/basemap/users/mapsetup.html # for other projections.  #proj = ccrs.PlateCarree() 
	#proj = 'moll'
	
    #proj  = 'cyl'
    #proj  = 'moll'
    proj  = 'cyl'
    
    #Define latitudes to plot (-90,90)
    #-90
    lat_i =   -60
    #90
    lat_f =  15
    
    #Define longitudes  to plot (-180,180)
    lon_i =  -90#240.0 
    lon_f =  -30
    
    m = Basemap(projection=proj, llcrnrlat=lat_i, urcrnrlat=lat_f,\
                llcrnrlon=lon_i, urcrnrlon=lon_f, resolution='c', lon_0=0)
    
    #m = Basemap(projection='moll', llcrnrlat=-90, urcrnrlat=90,\
    #            llcrnrlon=0, urcrnrlon=360, resolution='c', lon_0=0)
    
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawcountries()
    #m.drawstates()
    m.drawparallels(np.arange(-60.,60.,30.),labels=[1,0,0,0]) # draw parallels
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1]) # draw meridians
    
    # Make the plot continuous
    #air_cyclic, lons_cyclic = addcyclic(datatoplot, lons[:])
    # Shift the grid so lons go from -180 to 180 instead of 0 to 360.
    #air_cyclic, lons_cyclic = shiftgrid(180., air_cyclic, lons_cyclic, start=False)
    # Create 2D lat/lon arrays for Basemapnc_f = './air.sig995.2012.nc'  # Your filename
    lon2d, lat2d = np.meshgrid(lons, lats[:])
    # Transforms lat/lon into plotting coordinates for projection
    x, y = m(lon2d, lat2d)
    
    #numero de contornos
    # Plot of air temperature with 11 contour intervals
    
    #Parâmetros nc = np.linspace(limite inferior, limite superior, número de cores que a paleta irá conter)
    #Se: Terceiro parâmetro = (distância em módulo entre o segundo parâmetro e primeiro parâmetro) + 1
    #A escala será composta por valores exatos 
#    ncon = np.linspace(-15,15, 31, endpoint=True)
    ncon = np.arange(-6,7,1)
    cs = m.contourf(x, y, datatoplot, ncon, cmap=plt.cm.Spectral_r)
    cs = m.contourf(x, y, datatoplot, ncon, cmap=colorpallet)
   # cs = m.contourf(x, y, datatoplot, ncon, cmap= colorpallet)
#    cs = m.contourf(x, y, datatoplot, ncon, cmap='RdBu')
#    cs = m.contourf(x, y, datatoplot, 11, cmap='autumn', extend='both')
	# ticks = ncon[::n], n = distância entre cada escala
    cbar = plt.colorbar(cs,ticks=ncon[::4], orientation='horizontal', shrink=0.5)
    #cbar.set_label("%s (%s)" % (nc_fid.variables['air'].var_desc,\
    #                            nc_fid.variables['air'].units))
    #plt.title("%s on %s" % (nc_fid.variables['air'].var_desc, cur_time))
    plt.title("%s"%(plotname))
    
    
   
   #plt.savefig('%s.pdf'%(figname),bbox_inches='tight', format='pdf', dpi=1000)
    plt.savefig('%s'%(figname), dpi=1000)
    #media de cada estacao 

    plt.show()
    
    return fig     
   






	       
