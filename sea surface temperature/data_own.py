
#data: Data de interesse para plotar
#time: Vetor de tempo que será utilizado para procupar a data especificada acima



def data_day(data,time):

	index=0
	
	for i in range(0,len(time)): 
	    #print(data,time[i])
	    if(data==time[i]):
	        print('index=%s'%(i),data)
	        index=i
	        break
	if index==0:
		print('Fora de alcance')
	return index
	
	
	


	
	
	
	
	

