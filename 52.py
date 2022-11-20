numbers = []

for i in range(3):
    entry = input("Entry : ")
    # entry = int(entry)
    try:
        entry = float(entry)
        if str(entry)[-2:] == ".0":
            numbers.append(int(entry))
        else:
            numbers.append(entry)

    except ValueError:
        print("Entry must be a number")
    # finally:
    #     print("Hello from finally")
print(numbers)
