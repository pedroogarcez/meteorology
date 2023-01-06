from netCDF4 import num2date
from function import filename2
import datetime as dt
from cftime import num2pydate
from data_own import data_day
#import nc_time_axis
import numpy as np
import matplotlib.pyplot as plt

'''
Plot temporal de uma região especifica (retangulo de lats e lons)
Para realizar nosso plot temporal, possuímos dois caminhos: 
1: Plotar coordenadas específicas para todo intervalo de tempo;
2: Delimitar um retângulo com coordenadas específicas e calcular a média das latitudes e longitudes que compõe esse intervalo.
Vale ressaltar que o segundo meio é o mais seguro, haja visto que iremos trabalhar com a media das latitudes e a media das longitudes dentro do retangulo que foi criado.
'''

arquivo = 'ersst.v5.1891_2007.nc'
nc_f = arquivo
#lats, lons, time, sst = filename3(nc_f)
lats, lons, time, sst, lev = filename2(nc_f)

#Adaptando o vetor dt_time para o arquivo com variável DIÁRIA
dt_time = [dt.date(1891, 1, 1) + dt.timedelta(hours=t/60)
           for t in time]
units = "minutes since 1891-01-01 00:00"
calendar = 'gregorian'
dt_time2 = num2date(time, units=units, calendar=calendar)
print(dt_time2)

#Nino3: 5N-5S, 170W-90W
nino1 = {'name': 'El Niño 3.4', 'lat': -5, 'lon': 170}
nino2 = {'name': 'El Niño 3.4', 'lat': 5, 'lon': 190}

#Criando o retangulo pde acordo com as latitudes e longitudes espcificas:
lat1 = np.abs(lats - nino1['lat']).argmin()
lon1 = np.abs(lons - nino1['lon']).argmin()
lat2 = np.abs(lats - nino2['lat']).argmin()
lon2 = np.abs(lons - nino2['lon']).argmin()

#Calculando a media do intervalo de latitude especifico que foi determinado acima:
medialat = np.ma.mean(sst[:,:,lat1:lat2,:],axis=1)


#Após calcular a média acima, deixamos de ter um cubo por tres dimensões e passamos a ter um retangulo bidimensional: lons e time (lats deixou de ser o intervalo de lat1 - lat2 e passou a ser um ponto (média))

#A partir da media criada para latitude, calcula-se uma nova média. Como temos duas dimensões (lons e time), ao calcular a média para lons, teremos como resultado varios pontos em time representando a media de lat e lons.
#Media cubo -> Media quadrado -> Linha
mediaquadrado = np.ma.mean(medialat[:,:,lon1:lon2],axis = 1)
#print(mediaquadrado)

#Anomalia: (SON NINO3 1891 - SON NINO3 1891_2007, SON NINO3 1892 - SON NINO3 1891_2007)

#Calculando a média de cada ano
index1 = 8
index2 = 11
media_precip_son = []

for i in range(int((len(sst)-26*12)/12)):
    delta_data = mediaquadrado[index1:index2]
    #print(delta_data)
    media = np.ma.mean(delta_data)
    #print(media)
    media_precip_son.append(media)
    index1 += 12
    index2 += 12


#Calculando a média de do intervalo de tempo
set1891_2019 = np.mean(mediaquadrado[8::12])
out1891_2019 = np.mean(mediaquadrado[9::12])
nov1891_2019 = np.mean(mediaquadrado[10::12])
mediatrimestre1891_2019 = (set1891_2019+out1891_2019+nov1891_2019)/3.0

anomalia = media_precip_son - mediatrimestre1891_2019


'''
for i in range(0,len(dt_time2)):
    print(f'{dt_time2[i+12]} corresponde a {anomalia[i]} ')
'''
data = np.arange(1891,2007)
plt.plot(dt_time[0:len(dt_time2)-26*12:12],anomalia,'-o')
plt.plot(dt_time[0:len(dt_time2)-26*12:12],anomalia,'-o')
plt.axhline(0.0,linestyle='--')
plt.title('TSM Setembro-Outubro-Novembro')
plt.show()

