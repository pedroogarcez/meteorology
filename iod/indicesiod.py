import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Criando o data frame
df = pd.read_csv('indian-ocean-dipole-iod (1).csv')

plt.figure(figsize=(15,8))

#Transformando a data em datetime64
df['Data'] = df['DateTime'].astype('datetime64')

#Convertendo para lista os valores de indices e datas
datas = df['Data'].tolist()
iodindex = df['índice'].tolist()

dt_time = datas[252:1800]
iod = iodindex[252:1800]

#Configurando o plot 1700-2022
#plt.axhline(0,linestyle='--',color='k')
#plt.plot(datas,iodindex)

#Configurando o plot 1891-2019
#ano1891_2019 = plt.plot(dt_time,iod)

#Agora, vamos selecionar os valores do índice IOD referentes aos meses de Janeiro, Fevereiro e Março

iodJFM = []
index1 = 0
index2 = 3

for i in range(int(len(dt_time)/12)):
	mediaJFM = np.mean(iod[index1:index2:1])
	iodJFM.append(mediaJFM)
	index1 += 12
	index2 += 12
	
#Criando o eixo x para o gráfico iod média JFM
datamediaJFM1891_2019 = dt_time[0:len(dt_time):12]


#Construindo o gráfico
plt.plot(datamediaJFM1891_2019,iodJFM)
print(len(datamediaJFM1891_2019))


plt.show()
