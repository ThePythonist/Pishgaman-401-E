n = int(input("Enter any number : "))
# divisors = []

# for i in range(1,n+1):
# 	if n % i == 0 :
# 		divisors.append(i)


divisors = [ i for i in range(1,n+1) if n % i == 0 ]
print(divisors)


# if len(divisors) == 2 :
# 	print("The number is prime")
# else :
#         print("The number isn't prime")

if divisors == [1,n] :
	print("The number is prime")
else :
        print("The number isn't prime")
