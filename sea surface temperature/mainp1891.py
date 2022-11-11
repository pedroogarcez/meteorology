from netCDF4 import Dataset
from function import filename2
import datetime as dt  
from plot import plot_own,plot_media,plot_anom
from data_own import data_day
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

'''
Plot temporal de uma região especifica (retangulo de lats e lons)
Para realizar nosso plot temporal, possuímos dois caminhos: 
1: Plotar coordenadas específicas para todo intervalo de tempo;
2: Delimitar um retângulo com coordenadas específicas e calcular a média das latitudes e longitudes que compõe esse intervalo.
Vale ressaltar que o segundo meio é o mais seguro, haja visto que iremos trabalhar com a media das latitudes e a media das longitudes dentro do retangulo que foi criado.
'''

arquivo = 'ersst.v5.1891.nc'
nc_f = arquivo
#lats, lons, time, sst = filename3(nc_f)
lats, lons, time, sst, lev = filename2(nc_f)
#data = np.ma.maskedarray.tolist()




#Adaptando o vetor dt_time para o arquivo com variável DIÁRIA
dt_time = [dt.date(1891, 1, 1) + dt.timedelta(hours=t/58.0)
           for t in time]


nino1 = {'name': 'El Niño 3.4', 'lat': -5, 'lon': 190}
nino2 = {'name': 'El Niño 3.4', 'lat': 5, 'lon': 240}

#Criando o retangulo pde acordo com as latitudes e longitudes espcificas:
lat1 = np.abs(lats - nino1['lat']).argmin()
lon1 = np.abs(lons - nino1['lon']).argmin()
lat2 = np.abs(lats - nino2['lat']).argmin()
lon2 = np.abs(lons - nino2['lon']).argmin()


#Calculando a media do intervalo de latitude especifico que foi determinado acima:
medialat = np.mean(sst[:,lat1:lat2,:],axis=1)
#Após calcular a média acima, deixamos de ter um cubo por tres dimensões e passamos a ter um retangulo bidimensional: lons e time (lats deixou de ser o intervalo de lat1 - lat2 e passou a ser um ponto (média))

#A partir da media criada para latitude, calcula-se uma nova média. Como temos duas dimensões (lons e time), ao calcular a média para lons, teremos como resultado varios pontos em time representando a media de lat e lons.
#Media cubo -> Media quadrado -> Linha
mediaquadrado = np.mean(medialat[:,lon1:lon2],axis = 1)


