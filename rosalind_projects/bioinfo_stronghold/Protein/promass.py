import re
import pandas as pd
import numpy as np

Massround = []
promasstotal = 0

file = input("What is your file name?: ")

f = open(file, 'r')

aamass2 = pd.read_csv('aa_masstable_2.csv')

AA = aamass2['AA'].tolist()
Mass = aamass2['Mass'].tolist()


massdict = {}
for i in range(0,len(AA)):
    massdict[AA[i]] = Mass[i]
print(massdict)

Protein = f.read()
Prosplit = re.findall('.{1}', Protein)
print(Prosplit)

test = []
for item in Prosplit:
	for k,v in massdict.items():
		if k == item:
			test += [v]
			promasstotal += v
print(test)
print("%.3f" % round(promasstotal,3))
