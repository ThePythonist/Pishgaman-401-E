def f(x, y):
    if y == 1:
        return x + 1
    else:
        return 1 + f(x, y - 1)


print(f(2, 4))
