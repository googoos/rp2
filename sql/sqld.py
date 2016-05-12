import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    employees = csv.reader(open("employees.csv", "rU"))
    # c.execute("CREATE TABLE employees(firstname, lastname)")
    c.executemany("INSERT INTO employees(firstname, lastname) \
        values (?, ?)", employees)
