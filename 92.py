lines = open("words.txt").readlines()
sub_lst = [i for i in lines if i[-4:-1] == "ing"]
print(*sub_lst)
