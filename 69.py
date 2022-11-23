def func(x, y):
    # print(list(range(x, y)))

    print(*range(x, y))


a, b = int(input("Start : ")), int(input("End : "))
func(y=b, x=a)
