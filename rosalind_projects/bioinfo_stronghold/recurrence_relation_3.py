n = 5
k = 3
start = 1
generations = {}
rabbit_count = {}

for i in range (n):

	if i == 0:
		rabbit_count['baby', 'adult'] = start, 0
		generations['gen', i] = rabbit_count

	elif i > 0:
		if 'baby' in rabbit_count != 0:
			rabbit_count['adult'] += baby
		rabbit_count['baby'] = rabbit_count['adult'] * k
		generations['gen', i+1] = rabbit_count