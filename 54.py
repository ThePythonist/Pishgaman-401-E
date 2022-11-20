key = input("Enter any key to search in database : ")

info = {
    "name": "sony",
    "field": "technology",
    "city": "tokyo"
}

if key in info.keys():
    print("Found : ",info[key])
else :
    print("Not found")

# for i in info.keys():
#     if i == key:
#         print("Found", key)
#         break
# else:
#     print("Not Found")
