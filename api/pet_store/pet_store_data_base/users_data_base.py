import logging
import sqlite3
# from pet_store_data_base import PetStoreDataBase



class UserDataBase():

    """
    This class manages initiating new users database by creating new tables and adding
    new users to these tables.
    """
    def __init__(self, db_file):
        # super().__init__(db_name)
        self._db_file = db_file
        self.connection = None
        self.cur = None
        # self.cur = self.conn.cursor()
        # self._user_id = user_id
        # self._username = username
        # self._firstname = firstname
        # self._lastname = lastname
        # self._user_status = user_status

    def create_connection(self):
        try:
            logging.info("Creating connection in process.")
            self.connection = sqlite3.connect(self._db_file)
        except sqlite3.Error as error:
            logging.error(f'Creating connection failed: {error}')

    def close_connection(self):
        if self.connection:
            logging.info("Closing connection in process.")
            self.connection.close()


    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as error:
            logging.error(f'Executing query failed: {error}')

    def execute_read_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as error:
            logging.error(f'Executing query failed: {error}')
            return None

    def create_users_table(self, create_table_sql):
        self.execute_query(create_table_sql)




    # @property
    # def user_id(self):
    #     return self._user_id
    #
    # @user_id.setter
    # def user_id(self, value):
    #     self._user_id = value
    #
    # @property
    # def username(self):
    #     return self._username
    #
    # @username.setter
    # def username(self, value):
    #     self._username = value
    #
    # @property
    # def firstname(self):
    #     return self._firstname
    #
    # @firstname.setter
    # def firstname(self, value):
    #     self._firstname = value
    #
    # @property
    # def lastname(self):
    #     return self._lastname
    #
    # @lastname.setter
    # def lastname(self, value):
    #     self._lastname = value
    #
    # @property
    # def user_status(self):
    #     return self._user_status
    #
    # @user_status.setter
    # def user_status(self, value):
    #     self._user_status = value

    # --------------------------------------------------------------------------------------


        # try:
        #     logging.info("Creating table in process.")
        #     # Drop the users table if it exists
        #     self.cur.execute('DROP TABLE IF EXISTS users')
        #     # Create the users table with the correct schema
        #     self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
        #                      id INTEGER PRIMARY KEY,
        #                      username TEXT,
        #                      firstname TEXT,
        #                      lastname TEXT,
        #                      userStatus INTEGER)''')
        # except sqlite3.Error as error:
        #     logging.error(f'Creating table failed: {error}')

    # --------------------------------------------------------------------------------------

    # def add_user_to_table(self):
    #     try:
    #         logging.info("Adding new user to the table in process.")
    #         self.cur.execute('''
    #             INSERT INTO users (id, username, firstname, lastname, userStatus)
    #                          VALUES (?, ?, ?, ?, ?)''',
    #                          (self._user_id, self._username, self._firstname, self._lastname, self._user_status))
    #     except sqlite3.Error as error:
    #         logging.error(f'Adding user failed: {error}')
    #
    #     # Commit the transaction
    #     self.conn.commit()

    # --------------------------------------------------------------------------------------

    # def fetch_users(self):
    #     # Read data from the users table
    #     self.cur.execute("SELECT * FROM users")
    #     rows = self.cur.fetchall()
    #     for row in rows:
    #         print(row)
    #         logging.info(f'Added user: {row}')
    # --------------------------------------------------------------------------------------



    # --------------------------------------------------------------------------------------

    # def creating_full_process(self):
    #     self.create_users_table()
    #     self.add_user_to_table()
    #     self.fetch_users()
    #     self.close_connection()



# if __name__ == '__main__':
#     user = UserDataBase(2, 'admin', 'admin', 'admin', 1)
#     user.creating_full_process()