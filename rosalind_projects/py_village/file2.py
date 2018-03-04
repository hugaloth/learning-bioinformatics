text1 = open('rosalind_ini5.txt', 'r')


text1v = text1.readlines()

for i in range(1, 1+len(text1v)):
	if i%2==0:
		print(text1v[i-1])
	elif i%2==1:
		continue
