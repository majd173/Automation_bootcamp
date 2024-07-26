import logging
import sqlite3


# from pet_store_data_base import PetStoreDataBase


class UserDataBase:
    """
    This class manages initiating new users database by creating new tables and adding
    new users to these tables.
    """

    def __init__(self, db_file):
        self._db_file = db_file
        self.connection = None
        self.cur = None

    # --------------------------------------------------------------------------------------

    def create_connection(self):
        """
        This function creates a connection to the database.
        """
        try:
            logging.info("Creating database connection in process.")
            self.connection = sqlite3.connect(self._db_file)
            if self.connection:
                logging.info("Database connection created.")
            else:
                logging.error("Database connection not created.")
        except sqlite3.Error as error:
            logging.error(f'Creating database connection failed: {error}')

    # --------------------------------------------------------------------------------------

    def close_connection(self):
        """
        This function closes the connection to the database.
        """
        if self.connection:
            logging.info("Closing database connection in process.")
            self.connection.close()

    # --------------------------------------------------------------------------------------

    def execute_query(self, query, params=None):
        """
        This function executes a query in the database.
        It takes a query and an optional list of parameters.
        """
        try:
            logging.info("Executing database query in process.")
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                logging.info("Database query executed.")
            self.connection.commit()
        except sqlite3.Error as error:
            logging.error(f'Executing database query failed: {error}')

    # --------------------------------------------------------------------------------------

    def execute_read_query(self, query, params=None):
        """
        This function executes a query in the database.
        It takes a query and an optional list of parameters.
        """
        try:
            logging.info("Executing database query in process.")
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as error:
            logging.error(f'Executing database query failed: {error}')
            return None

    # --------------------------------------------------------------------------------------

    def create_table(self, create_table):

        logging.info("Creating table in process.")
        self.execute_query(create_table)
        logging.info("Table created.")

    # --------------------------------------------------------------------------------------

    def fetch_users(self):
        """
        This function fetches all users from the database.
        """
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
            logging.info(f'Added user to database: {row}')
    # --------------------------------------------------------------------------------------
