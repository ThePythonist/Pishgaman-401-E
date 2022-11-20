length = int(input("Dict Length : "))

keys = []
values = []
for i in range(length):
    k = input("Key : ")
    v = input("Value : ")
    keys.append(k)
    values.append(v)

d = dict(zip(keys, values))
print(d)
#
# if len(d) == 0:
#     print("Empty")
# else:
#     print("Not Empty")

if not bool(d):
    print("Empty")
else:
    print("Not Empty")
