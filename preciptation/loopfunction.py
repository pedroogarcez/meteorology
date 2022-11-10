import numpy as np

#Loopmedia: Loop para uma região especifica
#Loopprecip: Loop para todas lats e todas lons

def loopmedia(dt_time,mediaquadrado):
	alljanuary = []
	allfebruary = []
	allmarch = []
	alltime = []
	alltrimestre = []
	firstmonth = -12
	secondmonth = 1
	thirdmonth = 2	
	for i in range(0,int(len(dt_time)/12)):
		soma_month = mediaquadrado[firstmonth]
		soma_month2 = mediaquadrado[secondmonth]
		soma_month3 = mediaquadrado[thirdmonth]
		trime =  (mediaquadrado[firstmonth]+mediaquadrado[secondmonth]+mediaquadrado[thirdmonth])/3.0
		firstmonth = firstmonth+12
		secondmonth = secondmonth+12
		thirdmonth = thirdmonth+12
		year = dt_time[firstmonth]
		alljanuary.append(soma_month)
		allfebruary.append(soma_month2)
		allmarch.append(soma_month3)
		alltime.append(year)
		alltrimestre.append(trime)
	mediajaneiro = np.mean(alljanuary)
	mediafev = np.mean(allfebruary)
	mediamarco = np.mean(allmarch)
	mediatotalmeses = (mediajaneiro+mediafev+mediamarco)/3.0
	print(alltime)
	
	return alltime, alltrimestre, mediatotalmeses


def loopprecip(dt_time, precip,index1,index2,index3):
	alljanuary = []
	allfebruary = []
	allmarch = []
	alltime = []
	alltrimestre = []
	firstmonth = 0
	secondmonth =1
	thirdmonth = 2	
	for i in range(0,int(len(dt_time)/12)):
		soma_month = precip[firstmonth,:,:]
		soma_month2 = precip[secondmonth,:,:]
		soma_month3 = precip[thirdmonth,:,:]
		firstmonth = firstmonth+12
		secondmonth = secondmonth+12
		thirdmonth = thirdmonth+12
		alljanuary.append(soma_month)
		allfebruary.append(soma_month2)
		allmarch.append(soma_month3)

	media = (precip[index1,:,:]+precip[index2,:,:]+precip[index3,:,:])/3.0
	media1 = np.mean(alljanuary,axis = 0)
	media2 = np.mean(allfebruary,axis = 0)
	media3 = np.mean(allmarch,axis = 0)
	mediatotal = (media1+media2+media3)/3.0
	return media, mediatotal
