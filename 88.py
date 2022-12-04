# f = open("words.txt", "r").readlines()
five_letters = []
with open("words.txt", "r") as f:
    f = f.readlines()
    for line in f:
        if len(line) == 6:
            five_letters.append(line)


print(five_letters)
