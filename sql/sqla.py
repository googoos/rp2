# Create an SQLite3 database and table

# import the SQLlite3 library
import sqlite3

"""
# create a new  database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create table
cursor.execute(CREATE TABLE population
				(city TEXT, state TEXT, population INT)
				)
# close the data base connection
conn.close()
"""

# Create Car DB
conn = sqlite3.connect("cars.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE inventory
				(make TEXT, model TEXT, quantity INT)
				""")
conn.close()
