numbers = []

for i in range(5):
	x = int(input("Enter any number : "))
	numbers += [x]

# maximum = 0

# for i in numbers :
# 	if i > maximum :
# 		maximum = i
# 		print("changed into",i)
# 	else :
# 		print("nothing changed here")

# print("Maximum is",maximum)

#----------------------------------------
# numbers.sort()
# print(numbers[-1])

#----------------------------------------
print(max(numbers))
