from netCDF4 import Dataset
from function import filename2
import numpy as np
import datetime as dt

arquivo = 'gpcc_precip_1891_2019.nc'
nc_f = arquivo

nc_fid = Dataset(arquivo, 'r')
lats, lons, precip, time = filename2(nc_f)

dt_time = [dt.date(1891, 1, 1) + dt.timedelta(hours=t)
           for t in time]

# Recortando os vetores para ter informções somente no intervalo de 1959 a 2000
precip = precip[108::] / 30.0
dt_time = dt_time[108::]
# print(len(precip))
print(lons)
exit()
'''
for i in range(len(precip)):
    print(f'A data {dt_time[i]} corresponde ao índice {precip[i,0,0]}')
'''

# Agora vamos criar o plot de linhas, referentes as coordenadas da região central de acordo com CHAN et al
# Objetivo: Plotar um gráfico de linhas da anomalia de Setembro - Outubro - Novembro no intervalo de 1959 - 2000

# Definindo a "Região Central"
# regiao = {'lat1': -5, 'lat2': -25, 'lon1': -69, 'lon2': -40}
regiao = {'lat1': -19.5, 'lat2': -25, 'lon1': 1200, 'lon2': 305}

# Determinando as coordenadas específicas
lat_idx1 = np.abs(lats - regiao['lat1']).argmin()
lat_idx2 = np.abs(lats - regiao['lat2']).argmin()
lon_idx1 = np.abs(lons - regiao['lon1']).argmin()
lon_idx2 = np.abs(lons - regiao['lon2']).argmin()
print(lat_idx1)
print(lat_idx2)
print(lon_idx1)
print(lon_idx2)