import pandas as pd
import os, sys
from netCDF4 import Dataset
from function import filename2
import numpy as np
import datetime as dt
from plot import plot_precip, plot_anom
from data_own import data_day
import matplotlib.pyplot as plt
from loopfunction import loopmedia
#from indicesiod import iod



#Arquivo que faz as medias de maneira manual
arquivo = 'gpcc_precip_1891_2019.nc'
nc_f = arquivo


#To show the file variables
nc_fid = Dataset(arquivo, 'r')  # Dataset is the class behavior to open the file
                             # and create an instance of the ncCDF4 class
#nc_attrs, nc_dims, nc_vars = ncdump(nc_fid)
lats, lons, precip, time = filename2(nc_f)
precip = precip[816:1308]/30.0


dt_time = [dt.date(1891, 1, 1) + dt.timedelta(hours=t)
           for t in time]


#Criando uma série temporal com as mesmas datas
dt_time_paper = dt_time[816:1308]



# --
#Agora vamos criar o plot de linhas, referentes as coordenadas da região central de acordo com CHAN et al
#Objetivo: Plotar um gráfico de linhas da anomalia de Setembro - Outubro - Novembro no intervalo de 1959 - 2000

#Definindo a "Região Central"
regiao = {'lat1': -5,'lat2': -25,'lon1': -69,'lon2': -40}

#Determinando a posição de nossas latitudes específicas em nosso vetor de latitudes (lats) para Cantareira,
lat_idx1 = np.abs(lats - regiao['lat1']).argmin()
lat_idx2 = np.abs(lats - regiao['lat2']).argmin()
lon_idx1 = np.abs(lons - regiao['lon1']).argmin()
lon_idx2 = np.abs(lons - regiao['lon2']).argmin()
#Calculando a média das latitude (cubo->retangulo)
medialat = np.ma.mean(precip[:,lat_idx1:lat_idx2,:],axis = 1)

#Calculnado a média da longitude
mediaquadrado = np.ma.mean(medialat[:,lon_idx1:lon_idx2],axis = 1)

# -- SELECIONANDO OS MESES DE JFM DE 1891 - 2019 NA REGIÃO SUDESTE
set1891_2019 = mediaquadrado[8::12]
out1891_2019 = mediaquadrado[9::12]
nov1891_2019 = mediaquadrado[10::12]

# -- (1) SELECIONANDO OS MESES DE SON CADA ANO NA REGIÃO CENTRAL
index1 = 8
index2 = 10
media_precip_son = []

for i in range(int(len(precip)/12)):
    delta_data = mediaquadrado[index1:index2]
    media = np.ma.mean(delta_data)
    media_precip_son.append(media)
    index1 += 12
    index2 += 12


# -- (2) CALCULANDO A MÉDIA DE MÉDIA DE TOD0 INTERVALO DE TEMPO NA REGIÃO CENTRAL

media_central_1891_2019 = np.mean(set1891_2019+out1891_2019+nov1891_2019)


#Anomalia = (1) - (2)
anomalia  = media_precip_son - media_central_1891_2019


#Criando o eixo x
data = dt_time_paper[0::12]

#plt.plot(data,anomalia)
plt.plot(data,media_precip_son)
#plt.axhline(0.0,linestyle='--')
plt.show()
exit()



anomalia = alltrimestre-mediatotalmeses
alltime = dt_time[0:1548:12]

#Plotando o gráfico de linhas de anomalia de precipitação para a região Sudeste do Brasil
plt.figure()
plt.plot(alltime,anomalia,color='k')
plt.axhline(0,linestyle='--')
plt.title('Precipitation anomaly of southeast Brazil',fontweight='bold')

#Plotando o mapa de precipitação de anomalia
#fig = plot_anom(anomalia,lats,lons,'Anomalia precipitação (mm/dia) verão (JFM) 1891-2019','anomprecip1891_2019')
plt.show()

