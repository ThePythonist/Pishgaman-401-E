def main():
    def register():
        username = input("Enter username : ").casefold()
        accounts = open("DB-USERS.txt", "r").readlines()
        for i in accounts:
            if username == i[:-1]:
                print("Username taken")
                register()
        password = input("Enter password : ")
        open("DB-USERS.txt", "a+").write(username + "\n")
        open("DB-PASSWORDS.txt", "a+").write(password + "\n")
        print("Registered user")

        return True

    # register()

    def login():
        db_usernames = open("DB-USERS.txt").readlines()
        db_passwords = open("DB-PASSWORDS.txt").readlines()
        users = [i[0:-1] for i in db_usernames]
        passwords = [i[0:-1] for i in db_passwords]
        accounts = dict(zip(users, passwords))

        username = input("Enter username : ").casefold()
        password = input("Enter password : ")

        if username in accounts:
            if password == accounts[username]:
                print("Successfully logged in")
            else:
                print("Password is incorrect")
                login()
        else:
            print("Username is incorrect")

    # login()

    entry = input("""
Type 1 to signup
Type 2 to signin to your account
: """)

    if entry == "1":
        register()
    elif entry == "2":
        login()
    else:
        print("Invalid input")
        main()


main()
