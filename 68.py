def sorty(lst):
    # lst.sort()
    # return lst[::-1]
    # return lst
    lst.sort(reverse=True)
    return lst


lst = [11, 5, 3, 4, 1, 2]
print(sorty(lst))
