
import numpy  as np 

import matplotlib as mpl

import matplotlib.pyplot as plt

#from  read_ncfiles import ncdump

#To import the library necessary to make the maps 

from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

from matplotlib.colors import LinearSegmentedColormap

#colorpallet = LinearSegmentedColormap.from_list('mycmap', ['navy','gray','purple','white','green','yellow','red'], N=256, gamma=1.0)
#colorpallet = LinearSegmentedColormap.from_list('mycmap', ['navy','purple','gray','red','white','blue','yellow','green','red'], N=256, gamma=1.0)
colorpallet = LinearSegmentedColormap.from_list('mycmap', ['yellow','red','white','blue','green'], N=256, gamma=1.0)
#cor mais forte ao redor do centro, para que haja maior contraste entre -2 e 2


#used the user parameter to plot(plotparameter.py)



def plot_own(datatoplot,lats,lons,plotname,figname):

	#3)To plot the medium temperature in Autumm 2012.  ################################################################### #open figure 
    fig = plt.figure() #Adjust the location of the interior of the figgure fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9) # Setup the map. See http://matplotlib.org/basemap/users/mapsetup.html # for other projections.  #proj = ccrs.PlateCarree() 
	#proj = 'moll'
	
    #proj  = 'cyl'
    #proj  = 'moll'
    proj  = 'cyl'
    
    #Define latitudes to plot (-90,90)
    
    lat_i =  -90 
    lat_f =   90
    
    #Define longitudes  to plot (0,360)
    lon_i =  00.0 
    lon_f =  360
    
    m = Basemap(projection=proj, llcrnrlat=lat_i, urcrnrlat=lat_f,\
                llcrnrlon=lon_i, urcrnrlon=lon_f, resolution='c', lon_0=0)
    
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawcountries()
    m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0]) # draw parallels
    m.drawmeridians(np.arange(-180.,180.,30.),labels=[0,0,0,1]) # draw meridians
    
    # Make the plot continuous
    #air_cyclic, lons_cyclic = addcyclic(datatoplot, lons[:])
    # Shift the grid so lons go from -180 to 180 instead of 0 to 360.
    #air_cyclic, lons_cyclic = shiftgrid(180., air_cyclic, lons_cyclic, start=False)
    # Create 2D lat/lon arrays for Basemapnc_f = './air.sig995.2012.nc'  # Your filename
    lon2d, lat2d = np.meshgrid(lons, lats[:])
    # Transforms lat/lon into plotting coordinates for projection
    x, y = m(lon2d, lat2d)
    
    #numero de contornos
    #Definindo a barra de cor
    ncon = np.linspace(-2, 2, 5, endpoint=True)
    #Definindo as cores do mapa
    cs = m.contourf(x, y, datatoplot, ncon, cmap=plt.cm.Spectral_r)
   # cs = m.contourf(x, y, datatoplot, ncon, cmap='RdBu')
   # cs = m.contourf(x, y, datatoplot, 11, cmap='autumn', extend='both')
    #cs = m.contourf(x, y, datatoplot, ncon, cmap=colorpallet)
    cbar = plt.colorbar(cs,ticks=ncon[::40], orientation='horizontal', shrink=0.5)
#    cbar = plt.colorbar(cs, orientation='horizontal', shrink=1.0)
    #cbar.set_label("%s (%s)" % (nc_fid.variables['air'].var_desc,\
    #                            nc_fid.variables['air'].units))
    #plt.title("%s on %s" % (nc_fid.variables['air'].var_desc, cur_time))
    plt.title("%s"%(plotname))
    
    
    plt.savefig('%s'%(figname), dpi=1000)
    plt.show()
    return fig
    
def plot_media(datatoplot,lats,lons,plotname,figname):

	#3)To plot the medium temperature in Autumm 2012.  ################################################################### #open figure 
    fig = plt.figure() #Adjust the location of the interior of the figgure fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9) # Setup the map. See http://matplotlib.org/basemap/users/mapsetup.html # for other projections.  #proj = ccrs.PlateCarree() 
	#proj = 'moll'
	
    #proj  = 'cyl'
    #proj  = 'moll'
    proj  = 'cyl'
    
    lat = np.linspace(-90,90,721)
    lon = np.linspace(0,360,1441)
    plot,lon = shiftgrid(180.,plot,lon,start=False)
    
    
    
    m = Basemap(projection=proj, llcrnrlat=-90, urcrnrlat=90,\
                llcrnrlon=-180, urcrnrlon=180, resolution='c', lon_0=0)
    
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
    #air_cyclic, lons_cyclic = shiftgrid(180., air_cyclic, lons_cyclic, start=False)
    # Create 2D lat/lon arrays for Basemapnc_f = './air.sig995.2012.nc'  # Your filename
    lon2d, lat2d = np.meshgrid(lons, lats[:])
    # Transforms lat/lon into plotting coordinates for projection
    x, y = m(lon2d, lat2d)
    
    #numero de contornos
    #Defifindo as características da barra de cores
    ncon = np.linspace(-44, 44, 89, endpoint=True)
    #Definindo as cores do mapa
    cs = m.contourf(x, y, datatoplot, ncon, cmap=colorpallet)
    #cs = m.contourf(x, y, air_cyclic, ncon, cmap='RdBu')
    #cs = m.contourf(x, y, air_cyclic, 11, cmap='autumn', extend='both')

    cbar = plt.colorbar(cs,ticks=ncon[::8], orientation='horizontal', shrink=0.5)
    #cbar.set_label("%s (%s)" % (nc_fid.variables['air'].var_desc,\
    #                            nc_fid.variables['air'].units))
    #plt.title("%s on %s" % (nc_fid.variables['air'].var_desc, cur_time))
    plt.title("%s"%(plotname))
    
    
    plt.savefig('%s'%(figname), dpi=1000)
    #media de cada estacao 
    #media anual 
    #plt.show()
    return fig    

def plot_anom(datatoplot,lats,lons,plotname,figname):

	#3)To plot the medium temperature in Autumm 2012.  ################################################################### #open figure 
    fig = plt.figure() #Adjust the location of the interior of the figgure fig.subplots_adjust(left=0., right=1., bottom=0., top=0.9) # Setup the map. See http://matplotlib.org/basemap/users/mapsetup.html # for other projections.  #proj = ccrs.PlateCarree() 
	#proj = 'moll'
	
    #proj  = 'cyl'
    #proj  = 'moll'
    proj  = 'cyl'
    
    #Define latitudes to plot (-90,90)
    
    lat_i =   -90 
    lat_f =   90
    
    #Define longitudes  to plot (0,360)
    lon_i =  0.0 
    lon_f =  360.0
    
    m = Basemap(projection=proj, llcrnrlat=lat_i, urcrnrlat=lat_f,\
                llcrnrlon=lon_i, urcrnrlon=lon_f, resolution='c', lon_0=0)
    
    #m = Basemap(projection='moll', llcrnrlat=-90, urcrnrlat=90,\
    #            llcrnrlon=0, urcrnrlon=360, resolution='c', lon_0=0)
    
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawcountries()
    m.drawstates()
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
    ncon = np.linspace(-3,3, 7, endpoint=True)
   # cs = m.contourf(x, y, datatoplot, ncon, cmap=plt.cm.Spectral_r)
   # cs = m.contourf(x, y, datatoplot, ncon, cmap= colorpallet)
    cs = m.contourf(x, y, datatoplot, ncon, cmap='RdBu')
#    cs = m.contourf(x, y, datatoplot, 11, cmap='autumn', extend='both')
	# ticks = ncon[::n], n = distância entre cada escala
    cbar = plt.colorbar(cs,ticks=ncon[::1], orientation='horizontal', shrink=0.5)
    #cbar.set_label("%s (%s)" % (nc_fid.variables['air'].var_desc,\
    #                            nc_fid.variables['air'].units))
    #plt.title("%s on %s" % (nc_fid.variables['air'].var_desc, cur_time))
    plt.title("%s"%(plotname))
    
    
   
   #plt.savefig('%s.pdf'%(figname),bbox_inches='tight', format='pdf', dpi=1000)
    plt.savefig('%s'%(figname), dpi=1000)
    #media de cada estacao 

    plt.show()
    
    return fig     
    
    
    
    


	       
    
    


	       
