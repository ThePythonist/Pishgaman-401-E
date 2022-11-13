items = ["Ford",56,3.5,True,"Omid",(),4]
numbers = []

for i in items :
	if type(i) == int or type(i) == float :
		numbers += [i]

print(numbers)