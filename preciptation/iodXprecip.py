from return_function import variavel_iod, variavel_precip
import matplotlib.pyplot as plt

indice_iod, anomalia_normalizada_iod = variavel_iod()
#print(indice_iod)
l,anomalia, anomalia_nomalizada_precip = variavel_precip()

fig,ax1 = plt.subplots(figsize=(13,5))
ax1.bar(l,anomalia_nomalizada_precip,label='Precipitação',color='k')
#ax1.bar(l,anomalia,label='Precipitação',color='k')
ax1.legend()
ax1.plot(l,anomalia_normalizada_iod,label='Dipolo do Índico',color='blue')
ax1.legend()
plt.show()





