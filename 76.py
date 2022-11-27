def main():
    def factorial(x):

        if x == 1:
            # return x
            return 1
        else:
            return x * factorial(x - 1)

    entry = input("Enter any number to see factorial : ")

    try:
        entry = int(entry)
        try:
            print(factorial(entry))
        except RecursionError as error:
            # if entry == 0:
            #     print("Factorial of zero is 1")
            # else:
            #     print("Factorial doesnt exist")
            print(error)

    except ValueError:
        print("Entry must be integer")


main()
