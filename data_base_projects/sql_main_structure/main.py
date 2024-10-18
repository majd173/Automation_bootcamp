import sqlite3

# Connect to a database (or create it)
connection = sqlite3.connect('example.db')

# Create a cursor object
cursor = connection.cursor()

cursor.execute('DROP TABLE users')
# Execute SQL commands
cursor.execute('CREATE TABLE IF NOT EXISTS users ('
               'id INTEGER PRIMARY KEY, name TEXT, age INTEGER, location TEXT)')

name = 'positive'
age = 31
location = 'horfiesh'



# Insert some data
cursor.execute("INSERT INTO users (name, age, location) VALUES (?, ?, ?)",
               (name, age, location))

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for rows in rows:
    print(rows)

# Commit changes and close the connection
connection.commit()
connection.close()


