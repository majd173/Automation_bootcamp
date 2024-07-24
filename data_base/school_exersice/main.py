import sqlite3

# Connect to a database (or create it)
conn = sqlite3.connect('school.db')
# Create a cursor object
cur = conn.cursor()

# Drop the users table if it exists
cur.execute('DROP TABLE IF EXISTS students')

# Create the users table with the correct schema
cur.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)')

# Commit changes
# conn.commit()

# frst_name = 'positive'
# first_grade = 99
#
# second_name = 'good'
# second_grade = 95
#
# third_name = 'smile'
# third_grade = 80

# Insert data into the users table
cur.execute("INSERT INTO students (id, name, grade) VALUES (1, 'first', 99)")
cur.execute("INSERT INTO students (id, name, grade) VALUES (2, 'second', 95)")
cur.execute("INSERT INTO students (id, name, grade) VALUES (3, 'third', 93)")

print("start")
# Read data from the users table
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

# conn.commit()
# conn.close()


# Update
cur.execute("UPDATE students SET grade = 87 WHERE name = 'third'")
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
print("After update")
for row in rows:
    print(row)

conn.commit()
conn.close()