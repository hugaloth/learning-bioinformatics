import re
from sys import argv

script,file = argv

hamming = 0
seqfile = []
indexer = []

with open(file, 'r') as f:
	for line in f:
		seqfile.append(line)


s1 = seqfile[0]
s2 = seqfile[1]

s1split = re.findall('.{1}', s1)
s2split = re.findall('.{1}', s2)

print(s1split,s2split)

for i,j in enumerate(s1split):
	indexer = indexer + [i]

print(indexer)

for i in indexer:
	if s1split[i] != s2split[i]:
		hamming += 1

print(hamming)