def variavel_iod():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # A partir dos dados disponibilizados pela

    # Criando o data frame
    df = pd.read_csv('/home/pedro/Desktop/repositorios/tutorial/newfile/iod/indian-ocean-dipole-iod (1).csv')

    plt.figure(figsize=(15, 8))

    # Transformando a data em datetime64
    df['Data'] = df['DateTime'].astype('datetime64')

    # Convertendo para lista os valores de indices e datas
    datas = df['Data'].tolist()

    iodindex = df['índice'].tolist()

    # print(datas[1080])
    # print(datas[1560])

    # Limitando nosso vetor data de 1960 a 2000
    dt_time = datas[1068:1560]
    iod = iodindex[1068:1560]

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
        iodSON.append(mediaJFM)
        index1 += 12
        index2 += 12

    # Criando o eixo x para o gráfico iod média JFM
    data1960_2000 = dt_time[0::12]
    media = np.mean(iodSON)
    desvio_padrao = np.std(iodSON)
    anomalia_nomalizada = (iodSON-media)/desvio_padrao


    # Construindo o gráfico
    '''
    plt.plot(data1960_2000, iodSON)
    plt.title('Dipolo de Índico JFM', fontweight='bold')
    plt.axhline(0.0, linestyle='--', color='r')
    '''
    # plt.show()
    return iodSON, anomalia_nomalizada

def variavel_precip():
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

    # Recortando os vetores para ter informções somente no intervalo de 1959 a 2000
    precip = precip[816:1308] / 30.0
    dt_time = dt_time[816:1308]
    # print(dt_time)
    '''
    for i in range(len(precip)):
        print(f'A data {dt_time[i]} corresponde ao índice {precip[i,0,0]}')
    '''

    # Agora vamos criar o plot de linhas, referentes as coordenadas da região central de acordo com CHAN et al
    # Objetivo: Plotar um gráfico de linhas da anomalia de Setembro - Outubro - Novembro no intervalo de 1959 - 2000

    # Definindo a "Região Central"
    regiao = {'lat1': -5, 'lat2': -25, 'lon1': -69, 'lon2': -40}

    # Determinando as coordenadas específicas
    lat_idx1 = np.abs(lats - regiao['lat1']).argmin()
    lat_idx2 = np.abs(lats - regiao['lat2']).argmin()
    lon_idx1 = np.abs(lons - regiao['lon1']).argmin()
    lon_idx2 = np.abs(lons - regiao['lon2']).argmin()

    # Calculando a média das latitude (cubo->retangulo)
    medialat = np.ma.mean(precip[:, lat_idx1:lat_idx2, :], axis=1)

    # Calculnado a média da longitude
    mediaquadrado = np.ma.mean(medialat[:, lon_idx1:lon_idx2], axis=1)
    # médiaquadrado: vetor temporal constituído pela média de precipição na área determinada

    # Selecionando cada mês no vetor temporal criado acima
    set1891_2019 = mediaquadrado[8::12]
    out1891_2019 = mediaquadrado[9::12]
    nov1891_2019 = mediaquadrado[10::12]
    listafinal = set1891_2019 + out1891_2019 + nov1891_2019
    sum = (set1891_2019 + out1891_2019 + nov1891_2019) / 3.0
    ponto = np.mean(sum)

    # -- SELECIONANDO OS MESES DE JFM DE 1891 - 2019 NA REGIÃO SUDESTE
    set1891_2019 = np.mean(mediaquadrado[8::12])
    out1891_2019 = np.mean(mediaquadrado[9::12])
    nov1891_2019 = np.mean(mediaquadrado[10::12])
    mediatrimestre1891_2019 = (set1891_2019 + out1891_2019 + nov1891_2019) / 3.0

    # -- (1) SELECIONANDO OS MESES DE SON CADA ANO NA REGIÃO CENTRAL
    index1 = 8
    index2 = 11
    media_precip_son = []


    for i in range(int(len(precip) / 12)):
        delta_data = mediaquadrado[index1:index2]
        # print(delta_data)
        media = np.ma.mean(delta_data)
        desvio_padrão = np.ma.std(delta_data)
        # print(media)
        media_precip_son.append(media)

        index1 += 12
        index2 += 12

    # print(media_precip_son)

    # -- (2) CALCULANDO A MÉDIA DE MÉDIA DE TOD0 INTERVALO DE TEMPO NA REGIÃO CENTRAL

    # Anomalia = (1) - (2)
    anomalia = media_precip_son - ponto
    desvio_padrao = np.sqrt(np.sum(anomalia**2)/len(anomalia))
    anomalia_nomalizada_precip = anomalia / desvio_padrao
    # Criando o eixo x
    data = dt_time[0::12]
    l = np.arange(1960, 2001, 1)
    return l, anomalia, anomalia_nomalizada_precip
