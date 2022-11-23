import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# A partir dos dados disponibilizados pela


# Criando o data frame
df = pd.read_csv('/home/pedro/Desktop/repositorios/tutorial/newfile/iod/indian-ocean-dipole-iod (1).csv')

plt.figure(figsize=(15,8))

# Transformando a data em datetime64
df['Data'] = df['DateTime'].astype('datetime64')

# Convertendo para lista os valores de indices e datas
datas = df['Data'].tolist()

iodindex = df['índice'].tolist()

#print(datas[1080])
#print(datas[1560])


#Limitando nosso vetor data de 1960 a 2000
dt_time = datas[1080:1560]
iod = iodindex[1080:1560]


'''
for i in range(11):
    print(f'A data {dt_time[i]} corresponde ao índice {iod[i]}')
'''

# Agora, vamos selecionar os valores do índice IOD referentes aos meses de Setembro, Outubro e Novembro

iodSON = []
index1 = 8
index2 = 11

for i in range(int(len(dt_time) / 12)):
    mediaJFM = np.mean(iod[index1:index2:1])
    print(iod[index1:index2])
    print(mediaJFM)
    iodSON.append(mediaJFM)
    index1 += 12
    index2 += 12

# Criando o eixo x para o gráfico iod média JFM
data1960_2000 = dt_time[0::12]

# Construindo o gráfico
'''
plt.plot(data1960_2000, iodSON)
plt.title('Dipolo de Índico JFM', fontweight='bold')
plt.axhline(0.0, linestyle='--', color='r')
'''
def plot_iod(eixox,eixoy):
    fig = plt.plot(eixox, eixoy)
    plt.title('Dipolo de Índico JFM', fontweight='bold')
    plt.axhline(0.0, linestyle='--', color='r')
    plt.show()
    return fig
plot_iod(data1960_2000,iodSON)

#plt.show()
