class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS coinflips (flip INTEGER)')

    def save_flips(self, flips):
        self.cursor.executemany('INSERT INTO coinflips VALUES (?)', ((flip,) for flip in flips))
        self.conn.commit()

    def load_flips(self):
        self.cursor.execute('SELECT flip FROM coinflips')
        return [flip[0] for flip in self.cursor.fetchall()]

    def close(self):
        self.conn.close()


class FlipPredictor:
    def __init__(self):
        self.history = []
        self.flips = []
        self.predictions = []
        self.model = ModelBuilder.build_model()
        self.db = DatabaseManager('coinflips.db')
        self.flips = self.db.load_flips()

    def update_flips(self, new_flip):
        self.flips.append(new_flip)
        self.db.save_flips([new_flip])

    # ... (rest of the code remains the same)
