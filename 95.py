# lines = open("words.txt").readlines()
# items = [i[0:-1] for i in lines]
# print(items)

lines = open("words.txt").read().replace("\n", "")
open("one_line", "w").write(lines)
print("Done")
