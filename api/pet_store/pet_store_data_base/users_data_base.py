import logging
import sqlite3
# from pet_store_data_base import PetStoreDataBase



class UserDataBase():

    """
    This class manages initiating new users database by creating new tables and adding
    new users to these tables.
    """
    def __init__(self, user_id, username, firstname, lastname, user_status, db_name='pet_store.db'):
        # super().__init__(db_name)
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
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

    # --------------------------------------------------------------------------------------

    def create_users_table(self):
        try:
            logging.info("Creating table in process.")
            # Drop the users table if it exists
            self.cur.execute('DROP TABLE IF EXISTS users')
            # Create the users table with the correct schema
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                             id INTEGER PRIMARY KEY,
                             username TEXT,
                             firstname TEXT,
                             lastname TEXT,
                             userStatus INTEGER)''')
        except sqlite3.Error as error:
            logging.error(f'Creating table failed: {error}')

    # --------------------------------------------------------------------------------------

    def add_user_to_table(self):
        try:
            logging.info("Adding new user to the table in process.")
            self.cur.execute('''
                INSERT INTO users (id, username, firstname, lastname, userStatus)
                             VALUES (?, ?, ?, ?, ?)''',
                             (self._user_id, self._username, self._firstname, self._lastname, self._user_status))
        except sqlite3.Error as error:
            logging.error(f'Adding user failed: {error}')

        # Commit the transaction
        self.conn.commit()

    # --------------------------------------------------------------------------------------

    def fetch_users(self):
        # Read data from the users table
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        for row in rows:
            logging.info(f'Added user: {row}')
    # --------------------------------------------------------------------------------------

    def close_connection(self):
        self.conn.close()

    # --------------------------------------------------------------------------------------

    def creating_full_process(self):
        self.create_users_table()
        self.add_user_to_table()
        self.fetch_users()
        self.close_connection()



if __name__ == '__main__':
    user = UserDataBase(1, 'admin', 'admin', 'admin', 1)
    user.create_users_table()
    user.add_user_to_table()
    user.fetch_users()
    user.close_connection()