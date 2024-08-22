import sqlite3 

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS news(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    news TEXT
                )
            """)
            
    def add_news(self, news):
        with self.connection:
            self.cursor.execute("INSERT INTO news (news) VALUES(?)", (news,))
            
    # def get_user(self, user_id):
    #     with self.connection:
    #         return self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
# name=Database('new.db')
# name.create_table()
# name.add_news('donier1')
# name.add_news('donier2')
# name.add_news('donier3')
