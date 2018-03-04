print("Enter two positive integers a and b, where a<b<10000: ")
a = int(input())
b = int(input())

if a > 10000:
	a = int(input("Please enter a positive integer value for a: "))
	
if b < a and b > 10000:
	b = int(input("Please enter a value greater than a and less than 10000: "))
	
add = 0
for i in range(a,b):
	if i%2 == 1:
		add = add + i
	else:
		continue

print(add)
