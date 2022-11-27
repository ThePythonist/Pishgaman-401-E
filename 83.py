# def check(word):
#     lst = []
#
#     for i in word:
#         if i not in lst:
#             lst.append(i)
#         else:
#             print("Harf", i, "Tekrari ast")
#
#     if len(lst) == len(word):
#         print("Tekrari nadasht")


check = lambda word: True if len(word) == len(set(word)) else False
print(check("Mohammad"))
