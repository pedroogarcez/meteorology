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
precip = precip/30.0


#Necessidade de arrumar dt_time
dt_time = [dt.date(1891, 1, 1) + dt.timedelta(hours=t) 
           for t in time]

print(dt_time)
exit()

#Objetivo: Calcular a anomalia referente a JFM de 2019
#AnomaliaJFM2019 = médiaJFM2019 - mediaJFM1891-2019

#1) Vamos calcular a média de 2019
#Selecioando os meses de JFM

date1= dt.date(2018,12,1)
date2 = dt.date(2019,2,1)
date3 = dt.date(2019,3,1)
index1 = data_day(date1,dt_time)
index2 = data_day(date2,dt_time)
index3 = data_day(date3,dt_time)

#Calculando a média do trimestre de 2019
media2019 = (precip[index1,:,:]+precip[index2,:,:]+precip[index3,:,:])/3.0

#Selecionando JFM no intervalo de 1891 até 2019
dez1891_2019 = precip[12:len(precip):12]
fev1891_2019 = precip[1:len(precip):12]
marco1891_2019 = precip[2:len(precip):12]


#Calculando a média referente a cada mes no intervalo 1891_2019
mediadez1891_2019 = np.mean(dez1891_2019,axis=0)
mediafev1891_2019 = np.mean(fev1891_2019,axis=0)
mediamarco1891_2019 = np.mean(marco1891_2019,axis=0)

#Calculando a média do trimestre 1891_2019
mediatrimestral1891_2019 = (mediadez1891_2019 + mediafev1891_2019 + mediamarco1891_2019)/3.0

#Calculando a anomalia trimestral JFM 1891_2019
anomJFM1891_2019 = media2019-mediatrimestral1891_2019
#Plotando o gráfico da anomalia da américa do sul
#fig = plot_anom(anomJFM1891_2019,lats,lons,'Anomalia precipitação (mm/dia) verão (DJF) 1891_2019','anomprecip1891_2019')




# --
#Agora vamos criar o plot de linhas, referentes as coordenadas do sistema cantareira
#Objetivo: Plotar um gráfico de linhas da anomalia de DJZ no intervalo de 1891-2019
#Anomalia = médiacantareiraDJF1891-2019 - médiatodosmesesglobalDJF1891-2019 
#Definindo as coordenadas do sistema cantareira
cant = {'name': 'Sistema Cantareira, Brazil', 'lat': -19.5, 'lon': -55}
cant2 = {'name': 'Sistema Cantareira, Brazil', 'lat': -25, 'lon': -40}


#Determinando a posição de nossas latitudes específicas em nosso vetor de latitudes (lats) para Cantareira, 
lat_idx1 = np.abs(lats - cant['lat']).argmin()
lat_idx2 = np.abs(lats - cant2['lat']).argmin()
lon_idx1 = np.abs(lons - cant['lon']).argmin()
lon_idx2 = np.abs(lons - cant2['lon']).argmin()

#Calculando a média das latitude (cubo->retangulo)
medialat = np.ma.mean(precip[:,lat_idx1:lat_idx2,:],axis = 1)

#Calculnado a média da longitude
mediaquadrado = np.ma.mean(medialat[:,lon_idx1:lon_idx2],axis = 1)
print(mediaquadrado)
exit()
#Agora, criamos um vetor que contém as médias da região do Sistema Cantareira. A anomalia de precipitação será calculada para esse espaço
'''
Anomalia de precipitação na região Sudeste = Média de precipitação JFM xxxx na região Sudeste (1) - Média de precipitação JFM 1891-2019 na região Sudeste (2)
'''

# -- (1)
#print(f'O elemento {mediaquadrado[i]} corresponde a {dt_time}[i]') for i in range(dt_time))
for i in range(len(dt_time)):
    print(f'O elemento {mediaquadrado[i]} corresponde a {dt_time[i]} ')
exit()



# -- (2) SELECIONANDO OS MESES DE JFM DE 1891 - 2019 NA REGIÃO SUDESTE
jan1891_2019 = mediaquadrado[0:len(precip):12]
fev1891_2019 = mediaquadrado[1:len(precip):12]
marco1891_2019 = mediaquadrado[2:len(precip):12]
media_cant_1891_2019_JFM = (jan1891_2019+fev1891_2019+marco1891_2019)/3.0

mediajaneiro = np.mean(jan1891_2019)
mediafevereiro = np.mean(fev1891_2019)
mediamarco = np.mean(marco1891_2019)
mediatotalmeses = (mediajaneiro+mediafevereiro+mediamarco)/3.0

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

