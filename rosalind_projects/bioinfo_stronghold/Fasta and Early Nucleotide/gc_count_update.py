from sys import argv

seq_dict = {}
header = []
header_count = 0
gc_percents = []
header_with_gc = []
highest = 0
max_gc = []

script, file = argv

f = open(file, 'r')

for line in f:
	if '>' in line:
		header += [line.strip()]
		seq_dict[header[header_count]]=''
		header_count += 1
			
	if '>' not in line:
		seq_dict[header[header_count-1]] += line.strip()
print(seq_dict)

def gc_percent_calc(input):

	seq_length = len(input)
	G = input.count('G')
	C = input.count('C')

	calcuation = ((G + C)/seq_length)*100

	return calcuation

for item in header:
	calculated = gc_percent_calc(seq_dict[item])
	gc_percents += [calculated]
	if calculated > highest:
		highest = calculated
		max_gc = [item, highest]

print("%s\n%.6f" %(max_gc[0], max_gc[1]))



# For GC, make a new dict with header and gc % value, then compare items in that dict