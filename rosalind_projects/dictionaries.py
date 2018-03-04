stringfile = open('rosalind_ini6.txt', 'r')
string = stringfile.read()
wordstring = string.split()
sdict = {}
for i in range (0, len(wordstring)):
	sdict[wordstring[i]] = wordstring.count(wordstring[i])
for k, v in sdict.items():
	print(k + ' ' + str(v))
