import sqlite3
import bcrypt


class User:
    def __init__(self, db_path="database.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Create user tab"""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT,
                department TEXT,
                password TEXT NOT NULL
            )
        """
        )
        self.conn.commit()

    def create_user(self, username, department, password, email=None):
        try:
            hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            self.cursor.execute(
                "INSERT INTO users (username, password, department, email) VALUES (?, ?, ?, ?)",
                (username, hashed_pass, department, email),
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("User already exists!")
            return False
        except sqlite3.Error as e:
            print(f"Error en la base de datos: {e}")
            return False

    def get_user(self, username):
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = ?", (username))
            return self.cursor.fetchone()
        except sqlite3.IntegrityError:
            print("El usuario no existe!")
            return False
        except sqlite3.Error as e:
            print(f"Error en la base de datos: {e}")
            return False

    def verify_user(self, username, password):
        self.cursor.execute("SELECT password FROM users WHERE username = ?", (username))
        row = self.cursor.fetchone()
        if not row:
            return False

        stored_hash = row[0]
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash)

    def __del__(self):
        self.conn.close()
        print("Se cerró la conexion con la base de datos.")
