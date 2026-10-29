import sqlite3

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect("Login.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            senha TEXT NOT NULL)''')
        self.conn.commit()

    def insert(self, parametros: tuple):
        self.cursor.execute("insert into usuarios (nome, email, senha) values (?, ?, ?)",
                            parametros)
        self.conn.commit()

