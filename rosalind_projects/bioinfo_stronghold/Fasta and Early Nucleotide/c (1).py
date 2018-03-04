wholeline = []
complete = {}
index = []
new = {}
gcdict ={}

def Rosalind():
    while 1:
        try:
            file = input('Type your file name: ')
            f = open(file,'r')
            break
        except IOError as e:
            print(e)
    for line in f:
        line = line.strip()
        wholeline.append(line)

    for idx,item in enumerate(wholeline):
        if '>' in item:
            index.append(idx)
    for i in range(len(index)):
        if i < len(index)-1:
            complete[wholeline[index[i]]]= wholeline[index[i] +1 : index[i+1]]
        else:
            complete[wholeline[index[i]]] = wholeline[index[i]+1:]
    for x,y in complete.items():
        new[x] = "".join(y)
    return new
print(Rosalind())
    # maximum = 0

    # for x,y in new.items():
    #     gccount = 100 * ((y.count('C') + y.count('G'))/len(y))
    #     if gccount  > maximum:
    #         maximum = gccount     
    
    # for x,y in new.items():
    #     if 100 * ((y.count('C') + y.count('G'))/len(y)) == maximum:
    #         a = x
    # print(a,':',maximum,'%')
    


# def function(header):
#     for 
#     gccount = 100 * ((new[header].count('C') + new[header].count('G'))/len(new[header]))
#     print(gccount,'%')

# function('>Rosalind_0808')









