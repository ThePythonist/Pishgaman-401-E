import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

# cur.execute("CREATE TABLE customers (name VARCHAR(50),age INT, phone VARCHAR(50));")
# cur.execute("INSERT INTO customers VALUES ('Arian',16,'09353334325');")
# cur.execute("INSERT INTO customers VALUES ('Sara',24,'09213378325');")
#
# cur.execute("DELETE FROM customers;")  # Deletes every record in table
# cur.execute("DROP TABLE customers;") # Deletes table
cur.execute("SELECT * FROM customers;")
records = cur.fetchall()
print(records)

con.commit()
con.close()
print('Done')
