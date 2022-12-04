lines = open("words.txt").readlines()
sub_lst = [ i for i in lines if i[:3] == "sub"]
print(*sub_lst)
