items = ["Ford",56,3.5,True,"Omid",(),4]
numbers = []

for i in items :
	if type(i) == str :
		numbers += [i]

print(numbers)