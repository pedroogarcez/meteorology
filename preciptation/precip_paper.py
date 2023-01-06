import pandas as pd
from netCDF4 import Dataset
from function import filename2
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.patches as mpatches



arquivo = 'gpcc_precip_1891_2019.nc'
nc_f = arquivo


nc_fid = Dataset(arquivo, 'r')
lats, lons, precip, time = filename2(nc_f)

dt_time = [dt.date(1891, 1, 1) + dt.timedelta(hours=t)
           for t in time]

#Recortando os vetores para ter informções somente no intervalo de 1959 a 2000
precip = precip[816:1308] / 30.0
dt_time = dt_time[816:1308]

'''
for i in range(len(precip)):
    print(f'A data {dt_time[i]} corresponde ao índice {precip[i,0,0]}')
'''

# Agora vamos criar o plot de linhas, referentes as coordenadas da região central de acordo com CHAN et al
# Objetivo: Plotar um gráfico de linhas da anomalia de Setembro - Outubro - Novembro no intervalo de 1959 - 2000


# Definindo a "Região Central"
regiao = {'lat1': -5, 'lat2': -25, 'lon1': -69, 'lon2': -40}

#Determinando as coordenadas específicas
lat_idx1 = np.abs(lats - regiao['lat1']).argmin()
lat_idx2 = np.abs(lats - regiao['lat2']).argmin()
lon_idx1 = np.abs(lons - regiao['lon1']).argmin()
lon_idx2 = np.abs(lons - regiao['lon2']).argmin()


# Calculando a média das latitude (cubo->retangulo)
medialat = np.ma.mean(precip[:, lat_idx1:lat_idx2, :], axis=1)

# Calculnado a média da longitude
mediaquadrado = np.ma.mean(medialat[:, lon_idx1:lon_idx2], axis=1)
#médiaquadrado: vetor temporal constituído pela média de precipição na área determinada


#Selecionando cada mês no vetor temporal criado acima
set1891_2019 = mediaquadrado[8::12]
out1891_2019 = mediaquadrado[9::12]
nov1891_2019 = mediaquadrado[10::12]
listafinal = set1891_2019+out1891_2019+nov1891_2019
sum = (set1891_2019+out1891_2019+nov1891_2019)/3.0
ponto = np.mean(sum)


# -- SELECIONANDO OS MESES DE JFM DE 1891 - 2019 NA REGIÃO SUDESTE
set1891_2019 = np.mean(mediaquadrado[8::12])
out1891_2019 = np.mean(mediaquadrado[9::12])
nov1891_2019 = np.mean(mediaquadrado[10::12])
mediatrimestre1891_2019 = (set1891_2019+out1891_2019+nov1891_2019)/3.0


# -- (1) SELECIONANDO OS MESES DE SON CADA ANO NA REGIÃO CENTRAL
index1 = 8
index2 = 11
media_precip_son = []

for i in range(int(len(precip)/12)):
    delta_data = mediaquadrado[index1:index2]
    #print(delta_data)
    media = np.ma.mean(delta_data)
    #print(media)
    media_precip_son.append(media)
    index1 += 12
    index2 += 12

#print(media_precip_son)

# -- (2) CALCULANDO A MÉDIA DE MÉDIA DE TOD0 INTERVALO DE TEMPO NA REGIÃO CENTRAL

# Anomalia = (1) - (2)
anomalia = media_precip_son - ponto

o = anomalia**2
print(o[0:3])
print(np.sum(o[0:3]))

# Criando o eixo x
data = dt_time[0::12]
l = np.arange(1960,2001,1)
plt.bar(l,anomalia)
#plt.plot(data, anomalia)
# plt.axhline(0.0,linestyle='--')
#plt.show()
print(len(anomalia))






# Plotando o gráfico de linhas de anomalia de precipitação para a região Sudeste do Brasil

fig, ax = plt.subplots()
proj = 'cyl'

lat_i = -90
lat_f = 90

lon_i = -180
lon_f = 180

m = Basemap(projection=proj, llcrnrlat=lat_i, urcrnrlat=lat_f, \
            llcrnrlon=lon_i, urcrnrlon=lon_f, resolution='c', lon_0=0)

m.drawcoastlines()
m.drawmapboundary()
m.drawcountries()
m.drawparallels(np.arange(-60., 60., 30.), labels=[1, 0, 0, 0])  # draw parallels
m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])  # draw meridians


rect=mpatches.Rectangle((-70,-25),30,20,
                        fill = False,
                        color = "purple",
                        linewidth = 2)
plt.gca().add_patch(rect)
#plt.show()
