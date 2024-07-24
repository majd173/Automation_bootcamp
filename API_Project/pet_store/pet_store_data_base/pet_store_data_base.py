# pet_store_data_base.py
import sqlite3

class PetStoreDataBase:
    def __init__(self, db_name='pet_store.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()
