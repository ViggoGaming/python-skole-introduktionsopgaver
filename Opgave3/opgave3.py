x = int(input("x="))

for i in range(2, x+1):
	print("{}: {}".format(str(i), ", ".join(list(map(str, [num*i for num in range(1, 10+1)])))))
