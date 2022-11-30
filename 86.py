# def f1(text):
#     text = text.split()
#     lengths = [len(i) for i in text]
#     longest = max(lengths)
#
#     for word in text :
#         if len(word) == longest:
#             return word
#
#
# txt = "Python is a good language"
# print(f1(txt))


# def f2(text):
#     text = text.split()
#     text.sort(key=len)
#     return text[-1]
#
#
# txt = "Python is a good language"
# print(f2(txt))

def f3(text):
    return max(text.split(), key=len)


txt = "Python is a good language"
print(f3(txt))
