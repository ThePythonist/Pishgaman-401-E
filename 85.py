a = int(input("Enter integer part : "))
b = int(input("Enter decimal part : "))

# print("{i}.{d}".format(i=a, d=b))
# print(f"Five plus ten is {a+b} and not {a*b}")
print(f"Five plus ten is {a+b} and not {[ i for i in range(5)]}")
print(f"{a}.{b}")
