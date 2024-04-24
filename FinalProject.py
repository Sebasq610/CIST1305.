#Sebastian Quesada Barona
#4/24/2024
#this program buys, views, and sells stocks the user added to a database using sqlite3

import sqlite3

conn = sqlite3.connect("stocks.db")

#function that adds a new stock into the database
def buy():
    data = conn.cursor()
    print("You have bought a new stock!")
    data.execute('''CREATE TABLE IF NOT EXISTS stocks(date, bors, symbol, qty real, price real)''')
    data.execute("INSERT INTO stocks VALUES ('2024-04-12','BUY','GME',100,10.86)")
    conn.commit()
    data.execute('SELECT * FROM stocks')
    for row in data.fetchall():
        print(row)

#function that views all the stocks in the database
def viewAll():
    data= conn.cursor()
    data.execute('SELECT * FROM stocks')
    for row in data.fetchall():
        print(row)

#function that views a specific stock in the database
def view():
    data= conn.cursor()
    data.execute('SELECT * FROM stocks WHERE symbol = "GME"')
    for row in data.fetchall():
        print(row)
    
#function that sells a stock in the database
def sell():
    data= conn.cursor()
    data.execute('DELETE FROM stocks WHERE symbol = "GME"')
    conn.commit()
    print("Congrats you have sold your stock!")

#main function that calls function menu and menu2 and menu2 takes an arguement
def main():
    opt= menu()
    menu2(opt)

#function that displays the menu of selections you have in the program and also loops if you put the wrong input in and returns an arguement
def menu():
    print("1. Buy a stock")
    print("2. View a stock")
    print("3. Sell a stock")

    opt = int(input("\nSelection options(1,2,3): "))
    while opt > 3 or opt < 1:
        print("\nThat is not an option!\n")
        
        print("1. Buy a stock")
        print("2. View a stock")
        print("3. Sell a stock")

        opt = int(input("\nSelection options(1,2,3): "))
    return opt

#takes the arguement from menu to take the user to their selected option and also has a submenu for option 2
def menu2(opt):
    if opt == 1:
        buy()
    elif opt == 2:
        subopt= submenu()
        if subopt == 1:
            viewAll()
        elif subopt == 2:
            view()
        elif subopt == 3:
            opt= menu()
            menu2(opt)
    elif opt == 3:
        sell()

#submenu for option 2 that gives the user three options to view all, view a specific stock, and to return to the original menu also carries an argument subopt
def submenu():
    print("\n1. View all stocks")
    print("2. Search a specific stock")
    print("3. Return")

    subopt= int(input("\nSelection options(1,2,3): "))
    while subopt > 3 or subopt < 1:
        print("\nThat is not an option!\n")

        print("1. View all stocks")
        print("2. Search a specific stock")
        print("3. Return")

        subopt= int(input("\nSelection options(1,2,3): "))
    return subopt

main()
conn.close()