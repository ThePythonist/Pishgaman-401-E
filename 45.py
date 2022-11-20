lst = [11,22,33,11,11,44,55,22,66]

# unique = []

# for i in lst :
# 	if i not in unique :
# 		unique += [i]

unique = list(set(lst))
unique.sort()
print(unique)
