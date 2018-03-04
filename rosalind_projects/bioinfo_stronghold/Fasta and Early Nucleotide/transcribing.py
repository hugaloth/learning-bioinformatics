DNAf = open('rosalind_rna.txt', 'r')

DNA = DNAf.read()

RNA = DNA.replace("T", "U")

print(RNA)