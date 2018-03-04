print("Enter a value between 0 and 1000:")
a = -1
b = -1

if a not in (0,1000):
 	a = int(input())

if b not in (0, 1000):
	b = int(input())

hyp = (a**2 + b**2)**0.5
hypsq = int(hyp**2)


print("Your hypotenuse square is" + " " + str(hypsq))