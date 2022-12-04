def register():
    username = input("Enter username : ").casefold()
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

    print(accounts)


login()
