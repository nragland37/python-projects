# sqlite 3 database
import sqlite3

# connect to database
conn = sqlite3.connect("Inventory.db")
# create a cursor
c = conn.cursor()

# **************************************************************
# create a table
c.execute(
    """ CREATE TABLE Inventory (
    item text,
    quantity integer,
    price real
)"""
)

# create a table if it doesn't exist
c.execute(
    """ CREATE TABLE IF NOT EXISTS Inventory (
    item text,
    quantity integer,
    price real
)"""
)

# drop a table
c.execute("DROP TABLE Inventory")

# drop a table if it exists
c.execute("DROP TABLE IF EXISTS Inventory")

# insert a row of data
c.execute("INSERT INTO Inventory VALUES ('book', 10, 5.99)")
c.execute("INSERT INTO Inventory VALUES ('paper', 20, 1.99)")

# fetch data
c.execute("SELECT * FROM Inventory")
result = c.fetchall()
for row in result:
    print(row)

# fetch data with a where clause
c.execute("SELECT * FROM Inventory WHERE item='book'")
result = c.fetchall()

# fetch data with a where clause and a placeholder
c.execute("SELECT * FROM Inventory WHERE item=?", ("book",))

# input data from user
name = input("Enter a product name: ")
price = float(input("Enter a price: "))
c.execute("INSERT INTO Inventory VALUES (?, ?)", (name, price))


# **************************************************************
# commit our command
conn.commit()
# close our connection
conn.close()
