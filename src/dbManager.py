import sqlite3

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect("Login.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''PRAGMA foreign_keys = ON;''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            senha TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS agendamento(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            data TEXT NOT NULL UNIQUE,
                            usuario_id INTEGER,
                            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                            )''')
        self.conn.commit()

    def create_usuario(self, parametros: tuple):
        self.cursor.execute("insert into usuarios (nome, email, senha) values (?, ?, ?)",
                            parametros)
        self.conn.commit()

    def select_acesso(self, dado, coluna="*", where="*"):
        self.cursor.execute(f"select {coluna} from usuarios WHERE {where} = (?)", (dado,))
        return self.cursor.fetchall()

    def select_meus_agendamentos(self, usuario_id):
        self.cursor.execute('''SELECT data FROM agendamento
        INNER JOIN usuarios ON agendamento.usuario_id = usuarios.id
        WHERE (usuarios.id) = ? ''', (int(usuario_id),))
        return self.cursor.fetchall()

    def agendar(self, data, usuario_id):
        try:
            self.cursor.execute('''INSERT INTO agendamento (data, usuario_id) values (?, ?)''', (data, usuario_id))
            self.conn.commit()
            return True
        except Exception as e:
            print("Erro:", e)
            return False

    def verificar(self, data):
        self.cursor.execute('''SELECT id FROM agendamento WHERE data = (?)''', (data,))
        return self.cursor.fetchall()

