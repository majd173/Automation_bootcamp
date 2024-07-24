import sqlite3
from pet_store_data_base import PetStoreDataBase


class UserDataBase(PetStoreDataBase):

    def __init__(self, user_id, username, firstname, lastname, user_status, db_name='pet_store.db'):
        super().__init__(db_name)
        self._user_id = user_id
        self._username = username
        self._firstname = firstname
        self._lastname = lastname
        self._user_status = user_status

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value

    def create_add_user_table(self):
        # Drop the users table if it exists
        self.cur.execute('DROP TABLE IF EXISTS users')

        # Create the users table with the correct schema
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                         id INTEGER PRIMARY KEY,
                         username TEXT,
                         firstname TEXT,
                         lastname TEXT,
                         userStatus INTEGER)''')

        self.cur.execute('''
            INSERT INTO users (id, username, firstname, lastname, userStatus)
                         VALUES (?, ?, ?, ?, ?)''',
                         (self._user_id, self._username, self._firstname, self._lastname, self._user_status))

        # Commit the transaction
        self.conn.commit()

    def fetch_users(self):
        print("start")
        # Read data from the users table
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        # self.conn.commit()
        print("User was added successfully")

# if __name__ == '__main__':
#     user = UserDataBase(1, 'admin', 'admin', 'admin', 1)
#     user.create_add_user_table()
#     user.fetch_users()
#     user.close()