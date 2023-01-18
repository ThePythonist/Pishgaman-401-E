import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()


def create_table(table_name, fields):
    columns = []

    for i in range(int(fields)):
        columns.append(input("Column : "))

    command = "CREATE TABLE {} {};".format(table_name, tuple(columns))

    cur.execute(command)

    con.commit()
    con.close()

    print("Done")


def select_from(table_name):
    cur.execute("PRAGMA table_info(movies);")
    fields = cur.fetchall()
    try:
        entry = input("Do you need any filter (yes/no) ? : ")
        if entry == "yes":
            column = input("Column : ")
            condition = input("Condition : ")

            command = f"SELECT * FROM {table_name} WHERE {column} {condition} ;"
            cur.execute(command)
            values = cur.fetchall()
            print(values)

        elif entry == "no":
            command = f"SELECT * FROM {table_name};"
            cur.execute(command)
            values = cur.fetchall()

            fields2 = []
            for i in range(len(fields)):
                fields2.append(fields[i][1])

            records = []

            for i in values:
                records.append(dict(zip(tuple(fields2), i, )))

            for i in records:
                print(i)

        else:
            print("Invalid input. Try again")
            select_from(input("Enter table name : "))
    except sqlite3.OperationalError as error:
        if "no such table" in error:
            print("Table not found. Try again:")


def insert(table_name):
    cur.execute("PRAGMA table_info(movies);")
    records = cur.fetchall()
    values = []

    for i in range(len(records)):
        entry = input(f"{records[i][1]} : ")
        values.append(entry)

    command = "INSERT INTO {} VALUES {};".format(table_name, tuple(values))
    cur.execute(command)
    con.commit()
    print("Done")


while True:
    action = input("Action ( 1 : create / 2 : select / 3 : insert ) : ").casefold()
    if action == "1":
        create_table(input("Enter table name : "), input("Enter number of table fields : "))
        break
    elif action == "2":
        select_from(input("Enter table name : "))
        break
    elif action == "3":
        insert(input("Enter table name : "))
        break
    else:
        print("Invalid input. Try again")
