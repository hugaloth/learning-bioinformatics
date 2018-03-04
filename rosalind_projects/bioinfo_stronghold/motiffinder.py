"""
The goal of this program is to take a .txt text file containing two lines, 
a DNA sequence string and a motif substring, and to determine the starting position of the motif
substring as it is found in the original DNA sequence string.

**The output should be a single line with motif starting positions separated by a space**
"""

from sys import argv

#Declaration of variables
found_motif = None
motif_index = []
adjusted_index = []
lines = []
for_print = ''
DNA = ''
motif = ''
i = 0

#Use of argv to retrieve file name when starting program in terminal
script, file = argv

#Opening of the text file stored in variable 'file' using argv
f = open(file, 'r')
#Strips each line of text file and adds to list called 'lines'
for line in f:
	line = line.strip()
	lines += [line]

#Assigns variable 'DNA' to the first line of text stored in index 0 of 'lines'
DNA = lines[0]
print(DNA)

#Assigns variable 'motif' to the second line of text stored in index 1 of 'lines'
motif = lines[1]
print(motif)

#Loops for the entire length of the string stored in variable 'DNA'
while i<len(DNA):
	"""Starts searching 'DNA' at index 'i'
	Finding index where substring stored in variable 'motif' begins 
	Stores value in 'found_motif'
	"""
	found_motif = DNA.find(motif,i)

	"""If value of 'found_motif' is already stored in 'motif_index', the loop will add to while-loop counter 'i'
	 This essentially skips the 'found_motif' value stored at that 'i' index of 'DNA'
	"""
	if found_motif == -1 or found_motif in motif_index:
		i += 1

	#If 'found_motif' does not qualify above, it is stored in 'motif_index'
	else:
		motif_index += [found_motif]
		i += 1

"""Adjust 'motif_index' values to a 1-based numbering scheme 
Rather than default python 0-based numbering scheme
Adjusted value stored in 'adjusted_index'
"""
for item in motif_index:
	item += 1
	adjusted_index += [item]

#Prints the values of adjusted_index as a single line with values separated by spaces
for item in adjusted_index:
	item = str(item)
	for_print += item + ' '

#Final output of program	
print(for_print)