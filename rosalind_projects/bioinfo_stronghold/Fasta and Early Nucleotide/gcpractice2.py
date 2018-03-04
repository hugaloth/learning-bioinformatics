gcf = open('rosalindGCpractice.txt', 'r')
fastaf = gcf.readlines()

fasta = []
header = []
lindex = []
seq = []
data = ''

#Generate the list that contains the stripped headers
for line in fastaf:
	line = line.strip()
	fasta.append(line)
print(fasta)

for line in fasta:
	if line[0] == '>':
		header.append(line)
print(header)

#Generates the indexes for headers within the fasta file
for item in header: 
	lindex.append(fasta.index(item))
print(lindex)

#Adding joined sequence to central variable "seq"
for idx in range(len(lindex)):
	x = (fasta[lindex[idx]+1:lindex[idx+1]])
	seq = seq + ''.join(x)
print(seq)