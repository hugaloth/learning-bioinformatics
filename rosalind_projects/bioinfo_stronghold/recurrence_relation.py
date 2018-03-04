n = 5
k = 3
month = 0
juvenile = 1
mature = 0
adult_counter = 1
breed_counter = 0
total = 0

"""
while month<n:

	if mature >= 0:
		print("### Generation %d ###" %month)
		if month ==1:
			month += 1
			continue
		mature += juvenile
		print("Mature: ", mature)
		juvenile = 0
		juvenile = k*mature
		print("Juvenile: ", juvenile)
		month += 1

		if month == 5:
"""
	

"""
if month == 0:
	print("### Generation %d ###" %month)
	print("Mature: ", mature)
	print("Juvenile: ", juvenile)
	month += 1

while month < n and month != 0:

	print("### Generation %d ###" %month)

	while adult_counter == 1:
		mature += juvenile
		juvenile = 0
		adult_counter -= 1
		

	while breed_counter == 1:
		juvenile = k*mature
		adult_counter += 1
		breed_counter -= 1
		

		print("Mature: ", mature)
		print("Juvenile: ", juvenile)

	if month <5:
		month += 1
		continue
	else:
		total = mature + juvenile

print(total)
"""