print('Bienvenue au autre defiér')
#Validating email adresses
def emailadress(num):
	'''
	This function is aimed at validating email adresses with the right domain
	'''
	S1 = ''
	S2 = input('Enter Number :')
	S3 = S1 + S2
	E = ''
	E2 = input('Enter Character :')
	E1 = E + E2
	E1 = E1.lower()
	Top_Domain  = ''
	Top_Domain2 = input('Enter Domain :')
	Top_Domain1 =Top_Domain+Top_Domain2
	t = S3 + '@' + E1 + '.' + Top_Domain1
	print(t)
	if 2<=len(Top_Domain1)<=3:
		return True
	else:
		print('Invalid Format')
		if num == t :
			return 'Valid'
num = input('enter mail: ')	
emailadress(num)
print('Merci, a bientot !')

	
	