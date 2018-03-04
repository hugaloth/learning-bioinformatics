n = 5
k = 3
month = 0
juvenile = 1
juvenile_temp = 0
mature = 0
mature_temp	= 0
breeding = 0
breeding_temp = 0
rabbit_total = {}

rabbit_total['juvenile'] = juvenile
rabbit_total['mature'] = mature
rabbit_total['breeding'] = breeding

while month<n:

	if month == 0:
		print('### Generation %d ###' %month)
		print(rabbit_total)
		month += 1

	else:	
		print('### Generation %d ###' %month)
		
		breeding_temp += mature
		rabbit_total['breeding'] += breeding_temp

		mature_temp += juvenile
		rabbit_total['mature'] += mature_temp


		rabbit_total['juvenile'] += breeding*k
		rabbit_total['juvenile'] -= mature_temp

		mature_temp, breeding_temp, juvenile_temp = 0,0,0

		mature = rabbit_total['mature']
		breeding = rabbit_total['breeding']
		juvenile = rabbit_total['juvenile']

		rabbit_total['breeding'] = 0 
		month +=1		
		
		print(rabbit_total)
