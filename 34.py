numbers = [1,2,3,4,5]

for i in range(5):
    x = int(input("Enter a number between 6 - 10 : "))
    if 5 < x < 11 :
        numbers.append(x)

print(numbers)
