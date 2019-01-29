import sqlite3

connection = sqlite3.connect('data.sql')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# Example passing one element into the table
user = (0, 'Rick', 'running')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# Eample passing many elements into the table
users = [
  (1, 'Joe', 'password'),
  (2, 'Mike', 'pass123'),
  (3, 'Tim', 'pword!@#')
]

# Execute many rows 
cursor.executemany(insert_query, users)
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
  print(row)

connection.commit()
connection.close()