import sqlite3
from data_base.school_exersice import main

conn = sqlite3.connect('school.db')
cur = conn.cursor()

# Clean table
# cur.execute("DELETE from users")

# Create
cur.execute("INSERT INTO users (name, age, degree) VALUES ('positive', 30, 95)")
cur.execute("INSERT INTO users (name, age, degree) VALUES ('one', 25, 90)")
cur.execute("INSERT INTO users (name, age, degree) VALUES ('two', 20, 85)")

print("start")
# Read
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# # Update
# cur.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")
# cur.execute("SELECT * FROM users")
# rows = cur.fetchall()
# print("After update")
# for row in rows:
#     print(row)
#
# # Delete
# cur.execute("DELETE FROM users WHERE name = 'Bob'")
# cur.execute("SELECT * FROM users")
# rows = cur.fetchall()
# print("After delete")
# for row in rows:
#     print(row)

conn.commit()
conn.close()
