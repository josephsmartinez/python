import sqlite3

class User(object):
  def __init__(self, id, username, password):
    self.id = id
    self.username = username
    self.password = password

  @classmethod
  def find_by_username(cls, username):
    connection = sqlite3.connect('data.sql')
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username=?"
    # The comma tells python the () are a tuple
    result = cursor.execute(query, (username,))
    row = result.fetchone()
    if row:
      user = cls(row[0], row[1], row[2])
    else:
      user = None

    connection.close()
    return user

  @classmethod
  def find_by_id(cls, id):
    connection = sqlite3.connect('data.sql')
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE id=?"
    result = cursor.execute(query, (id,))
    row = result.fetchone()
    if row:
      user = cls(row[0], row[1], row[2])
    else:
      user = None

    connection.close()
    return user
        