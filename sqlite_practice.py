import sqlite3
conn = sqlite3.connect("login_database.db")
c = conn.cursor()

# c.execute("CREATE TABLE Persons (Personid INTEGER NOT NULL AUTO_INCREMENT, LastName TEXT NOT NULL,FirstName TEXT,Age INTEGER, PRIMARY KEY (Personid))")
c.execute("CREATE TABLE Persons (userid INTEGER NOT NULL AUTO_INCREMENT, first_name TEXT, last_name TEXT, emailid TEXT, age INTEGER, phonenumber INTEGER, city TEXT, PRIMARY KEY (userid)")

def insert_values_into_persons():
    c.execute('INSERT INTO userid (?, last_name, emailid, age, phonenumber, city) VALUES "Joe", "Smith", "joesmith@gmailcom",23,"401-452-4587", "SanFrancisco"), ("Peter", "Parker", "peter20@gmailcom",22, "957-568-1234", "New York"), ("Ross", "Cook", "ross123@gmailcom",26,"902-572-9857", "New York"), ("Emily", "Brown", "emilybrown5@gmailcom",27,"401-999-5252", "Boston"), ("Sasha", "Johnson", "sasha2345@gmailcom",21,405-145-2664", "San Jose"), ("Mary", "Hanks", "Maryh@gmailcom",23, "927-444-7563", "Boston")', (variable))


# def update_phon
conn.commit()
conn.rollback()
c.close()
conn.close()
conn = sqlite3.connect("login_database.db")
c = conn.cursor()
