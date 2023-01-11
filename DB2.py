import sqlite3

con = sqlite3.connect('test2.db')
cur = con.cursor()

# cur.execute("""
# CREATE TABLE employees (
# id INTEGER PRIMARY KEY,
# fname VARCHAR(50),
# lname VARCHAR(50),
# age INT,
# job VARCHAR(50)
# );
# """)
#
# people = [
#     {"Fname": "Sepideh", "Lname": "Hajimirzaei", "Age": 13, "Job": "Front-End Dev"},
#     {"Fname": "Nima", "Lname": "Aliyari", "Age": 16, "Job": "Front-End Dev"},
#     {"Fname": "Meysam", "Lname": "Davar", "Age": 18, "Job": "DB Man"},
#     {"Fname": "Kiarash", "Lname": "Sayas", "Age": 7, "Job": "Project Manager"},
#     {"Fname": "Amin", "Lname": "Sinaei", "Age": 16, "Job": "Security Engineer"},
# ]


# for person in people:
#     cur.execute(f"INSERT INTO employees(fname,lname,age,job) VALUES (?,?,?,?)",
#                 (person["Fname"], person["Lname"], person["Age"], person["Job"]))
#     con.commit()
cur.execute("INSERT INTO employees(fname,lname,age,job) VALUES ('Kia','Rezayi',21,'Front-End');")
# cur.execute("DELETE FROM employees;")
cur.execute("DELETE FROM employees WHERE fname='Kia';")
cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
print(len(records))
# print(records)
for record in records:
    print(record)

con.commit()
con.close()
print('Done')
