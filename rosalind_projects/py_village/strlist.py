string = input('Copy and paste string here:')
print("Input value for slicing integers a,b,c, and d respectively:")

a = int(input())
b = int(input())+1
c = int(input())
d = int(input())+1

index1 = string[a:b]
index2 = string[c:d]

print(index1 + " " + index2)