import sqlite3

print("1. Buy a stock")
print("2. Sell a stock")
print("3. Add a stock")
opt=input("Selection option(1,2,3): ")

for opt >= "1":
    buy()

def buy():

#Cretae a connection to the database
conn=sqlite3.connect("example.db")

#create a cursor
data = conn.cursor()

#var transaction_data, transaction_type, symbol, qty, price

#create a table
data.execute('''CREATE TABLE IF NOT EXISTS stocks(data text, trans text, symbol text, qty real, price real)''')

#insert a row of data
data.execute("INSERT INTO stocks VALUES ('2024-04-12','BUY','GME',100,10.86)")

#save (commit) the changes
conn.commit()


#Query the database
data.execute('SELECT * FROM stocks')

#print the results
for row in data.fetchall():
    print(row)

#close the connection
conn.close()
