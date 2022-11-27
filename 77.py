def f(x, y):
    if y == 1:
        return x
    else:
        return x + f(x, y - 1)


print(f(2, 4))
