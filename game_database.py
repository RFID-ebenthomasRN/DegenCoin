import sqlite3

class GameDatabase:
    def __init__(self, dbname='game.db'):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS coinflips (flip INTEGER)')

    def insert_flip_to_db(self, flip):
        query = "INSERT INTO coinflips (flip) VALUES (?)"
        self.cursor.execute(query, (flip,))
        self.conn.commit()

    def retrieve_flips_from_db(self):
        query = "SELECT * from coinflips"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_db(self):
        self.conn.close()