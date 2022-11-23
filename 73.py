def prime(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    print(divisors)
    # if len(divisors) == 2:
    #     return True
    # else:
    #     return False

    return "True" if len(divisors) == 2 else "False"
    # print("True") if len(divisors) == 2 else print("False")


x = 12
print(prime(x))
