n = int(input('How many months pass?: '))
k = int(input('How many pairs born per rabbit pair?: '))
rabbit_count = {}

for month in range(n):

	if month == 0:
		f1 = 1
		rabbit_count['month %d' %month] = f1

	if month == 1:
		f2 = 1
		rabbit_count['month %d' %month] = f2

	if month > 1:
		current = rabbit_count['month %d' %(month-2)]*k + rabbit_count['month %d' %(month-1)]
		rabbit_count['month %d' %month] = current

print('\n')
print('Total rabbit pairs for given parameters: ', rabbit_count['month %d' %(n-1)])