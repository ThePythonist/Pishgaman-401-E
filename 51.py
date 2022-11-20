entry = input("Entry : ")
# entry = int(entry)

try:
    entry = int(entry)
    print(entry, "Is a number")
except ValueError:
    print("Entry must be a number")
# finally:
#     print("Hello from finally")
