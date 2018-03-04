lst = []
f = open('rosalindGCpractice.txt','r')
for line in f:
	line = line.strip()
	if '>' in line:
		lst.append(line)
print(lst)


