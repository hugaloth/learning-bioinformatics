rawfile = open('rosalind_dna.txt', 'r')

DNAstring = rawfile.read()

A = DNAstring.count('A')
C = DNAstring.count('C')
G = DNAstring.count('G')
T = DNAstring.count('T')

bases = str(A)+' '+str(C)+' '+str(G)+' '+str(T)
print(bases)