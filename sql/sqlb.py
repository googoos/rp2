# INSERT Command

# import SQLite3 library
import sqlite3

"""
# 1
conn = sqlite3.connect("new.db")
cursor = conn.cursor()

# inser data
cursor.execute("INSERT INTO population VALUES('New York City', \
    'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Fransisco', \
    'CA', 8000000)")

conn.commit()
conn.close()
"""
"""
# 2
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', \
        'NY', 8200000)")
    c.execute("INSERT INTO population VALUES('San Fransisco', \
        'CA', 8000000)")
"""

# 3
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # insert multiple  records using a tuple
    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 2700000),
            ('Houston', 'TX', 2100000),
            ('Phoenix', 'AZ', 1500000)
            ]
    # insert data into table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
