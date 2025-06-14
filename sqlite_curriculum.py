import sqlite3
conn=sqlite3.connect('databasename.db')
c=conn.cursor()

try:
    c.execute('CREATE TABLE cars (column1 TEXT, column2, INTEGER)')
except sqlite3.OperationalError:
    pass

column1_values = ["Toyota", "Lexus", "Acura"]
column2_values = [23, 24, 21]

c.execute('INSERT INTO cars (column1, column2) VALUES (?, ?), (?, ?)', (column1_values[0], column2_values[0], column1_values[1], column2_values[1]))
c.execute('SELECT * FROM cars')

print(c)

for r in c:
    print(r[0], r[1])
conn.commit()
conn.rollback()
c.close()
conn.close()
