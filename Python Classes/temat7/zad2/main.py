import sqlite3

def check_tables(database):
    #na potrzeby zadania
    pass

def create_checker(connection):
    def checker():
        return check_tables(connection)
    return checker

conn = sqlite3.connect("jakasbaza.db")
checker = create_checker(conn)
checker()