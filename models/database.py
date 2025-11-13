import sqlite3
import bcrypt

from dataclasses import dataclass
from typing import Any, Optional

from .user import User


@dataclass
class Result:
    success: bool
    message: Optional[str] = None
    data: Optional[Any] = None


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

    def create_user(self, user: User) -> Result:
        try:
            hashed_pass = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
            self.cursor.execute(
                "INSERT INTO users (username, password, department, email) VALUES (?, ?, ?, ?)",
                (user.username, hashed_pass, user.department, user.email),
            )
            self.conn.commit()
            return Result(True, "Account created successfully")
        except sqlite3.IntegrityError:
            return Result(False, "Account already exists!")
        except sqlite3.Error as e:
            return Result(False, f"Database error: {e}")

    def get_user(self, username: str) -> Result:
        try:
            self.cursor.execute(
                "SELECT id, username, email, department FROM users WHERE username = ?",
                (username,),
            )

            row = self.cursor.fetchone()

            if not row:
                return Result(False, "Account does not exist")

            user = User(id=row[0], username=row[1], email=row[2], department=row[3])
            return Result(True, "User found", user)

        except sqlite3.IntegrityError:
            return Result(False, "Account does not exist!")
        except sqlite3.Error as e:
            return Result(False, f"Database error: {e}")

    def verify_user(self, username: str, password: str) -> Result:
        self.cursor.execute(
            "SELECT password FROM users WHERE username = ?", (username,)
        )

        row = self.cursor.fetchone()
        if not row:
            return Result(False, "Account does not exist")

        stored_hash = row[0]
        match = bcrypt.checkpw(password.encode("utf-8"), stored_hash)

        if not match:
            return Result(False, "Incorrect password")
        else:
            return Result(True, "User verified")

    def __del__(self):
        self.conn.close()
