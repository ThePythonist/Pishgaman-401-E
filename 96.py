lines = open("words.txt").readlines()
# rev = []
# for line in lines:
#     rev.append(line[::-1])
rev = [line[::-1] for line in lines]
output = "".join(rev)
open("reversed.txt", "w").write(output)
print("Done")