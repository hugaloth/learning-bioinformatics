def seqreading(file):
	seq=''
	with open(file, 'r') as f:
		for line in f:
			if not line[0] =='>':
				seq += line.rstrip()
	return seq

print(seqreading('rosalindGCpractice.txt'))
