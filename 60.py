# word = "python"
# d = {}
# n = 0
#
# for i in word:
#     d.setdefault(i, n)
#     n += 1
#
# print(d)

# -----------------------------------

word = "python"
d = {}

for i in range(len(word)):
    d.setdefault(word[i], i)

print(d)
