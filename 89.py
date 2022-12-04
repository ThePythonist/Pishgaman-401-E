# f = open("words.txt", "r").readlines()


# five_letters = ""
# with open("words.txt", "r") as f:
#     f = f.readlines()
#     for line in f:
#         if len(line) == 6:
#             five_letters += line
#
# open("five_letters.txt", "w").write(five_letters)
# print("Done")

five_letters = []
with open("words.txt", "r") as f:
    f = f.readlines()
    for line in f:
        if len(line) == 6:
            five_letters.append(line)

output = "".join(five_letters)
open("five_letters.txt", "w").write(output)
print("Done")


# In ravesh aslan khoob nist ! Zaman ziadi baraye ejra migire
# with open("words.txt", "r") as f:
#     f = f.readlines()
#     for line in f:
#         if len(line) == 6:
#             open("five_letters.txt", "a+").write(line)
#
# print("Done")
