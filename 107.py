from random import choice


# def generate1():
#     password = []
#
#     for i in range(6):
#         x = str(choice(range(10)))
#         password.append(x)
#
#     return "".join(password)
#
#
# print(generate1())

def generate2():
    password = ""

    for i in range(6):
        x = str(choice(range(10)))
        password += x

    return password


print(generate2())
