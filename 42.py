n = int(input("Enter a length : "))
numbers = []


for i in range(n):
	x = int(input("Enter any number : "))
	numbers.append(x)

print(max(numbers))
