# def check(word):
#     if len(word) == len(set(word)):
#         return True
#     else:
#         return False
#
#
# word = input("Entry : ")
# print(check(word))

def check(word):
    lst = []

    for i in word:
        if i not in lst:
            lst.append(i)
        else:
            print("Harf", i, "Tekrari ast")

    if len(lst) == len(word):
        print("Tekrari nadasht")


check("mohammad")
