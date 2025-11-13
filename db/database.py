import sqlite3
import bcrypt

from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    email: str
    department: str


class Database:
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
            return True, "Account created successfully", None
        except sqlite3.IntegrityError:
            return False, "Account already exists!", None
        except sqlite3.Error as e:
            return False, f"Database error: {e}", None

    def get_user(self, username):
        try:
            self.cursor.execute(
                "SELECT id, username, email, department FROM users WHERE username = ?",
                (username,),
            )
            row = self.cursor.fetchone()
            return (
                True,
                None,
                User(id=row[0], username=row[1], email=row[2], department=row[3]),
            )
        except sqlite3.IntegrityError:
            return False, "Account does not exist!", None
        except sqlite3.Error as e:
            return False, f"Database error: {e}", None

    def verify_user(self, username, password):
        self.cursor.execute(
            "SELECT password FROM users WHERE username = ?", (username,)
        )
        row = self.cursor.fetchone()
        if not row:
            return False

        stored_hash = row[0]
        match = bcrypt.checkpw(password.encode("utf-8"), stored_hash)

        return match

    def __del__(self):
        self.conn.close()
