# Ex 1

# def f(name):
#     return "Hello" + " " + name
#
#
# print(f("Farzad"))

# f = lambda name: "Hello" + " " + name
# print(f("Kiarash"))

# Ex 2 -----------------------------------------------------
# def f(x):
#     return "Even" if x % 2 == 0 else "Odd"
#
#
# print(f(int(input())))

# zoj_ya_fard = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(zoj_ya_fard(int(input("Entry : "))))

# Ex 3 -----------------------------------------------------
# def power(a, b):
#     return a ** b
#
#
# print(power(2, 4))

# power = lambda a, b: a ** b
# print(power(2, 3))

# Ex 4 -----------------------------------------------------
# def tavan(x, y):
#     if y == 1:
#         return x
#     else:
#         return x * tavan(x, y - 1)
#
#
# print(tavan(2, 4))

# tavan = lambda x, y: x if y == 1 else x * tavan(x, y - 1)
# print(tavan(2, 3))
