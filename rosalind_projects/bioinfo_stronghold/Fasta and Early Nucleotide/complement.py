DNAf = open('rosalind_revc.txt', 'r')
DNA = DNAf.read()

complement = DNA
cDNA = ('')
for i in range(0,len(DNA)):

	complement =  DNA[i]
	

	if complement == 'A':
		complement = complement.replace('A', 'T')
	elif complement =='T':
		complement = complement.replace('T', 'A')
	elif complement =='G':
		complement = complement.replace('G', 'C')
	elif complement =='C':
		complement = complement.replace('C', 'G')
	

	cDNA = cDNA+complement

print(cDNA)

rcDNA = cDNA[::-1]

print('Final: ', rcDNA)