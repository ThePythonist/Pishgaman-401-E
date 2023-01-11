import sqlite3

con = sqlite3.connect('Pishgaman-E.db')
cur = con.cursor()

# cur.execute("""
# CREATE TABLE students (
# id INTEGER PRIMARY KEY,
# fname VARCHAR(50),
# lname VARCHAR(50),
# age INT,
# major VARCHAR(70)
# );
# """)

# people = [
#     {"Fname": "Alireza", "Lname": "Mirzaei", "Age": 27, "Major": "Industrial Engineering"},
#     {"Fname": "Mohammad", "Lname": "Tahernejad", "Age": 19, "Major": "Computer Engineering"},
#     {"Fname": "Mohammadreza", "Lname": "Azimi", "Age": 13, "Major": "Computer Engineering"},
#     {"Fname": "Arash", "Lname": "Sadeghinejad", "Age": 21, "Major": "Software Engineering"},
# ]
#
# for person in people:
#     cur.execute(f"INSERT INTO students(fname,lname,age,major) VALUES (?,?,?,?)",
#                 (person["Fname"], person["Lname"], person["Age"], person["Major"]))
#     con.commit()
# cur.execute("INSERT INTO students(fname,lname,age,major) VALUES ('Kia','Rezayi',21,'Front-End');")

cur.execute("SELECT * FROM students ;")
records = cur.fetchall()

for i in records:
    print(i)

con.commit()
con.close()
print('Done')
