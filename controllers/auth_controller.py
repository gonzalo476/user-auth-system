import re

from models.database import Database, Result


class AuthController:
    def __init__(self):
        self.db = Database()

    def login(self, username: str, password: str):

        if not username or not password:
            return Result(False, "Invalid username or password")
        else:
            result = self.db.verify_user(username=username, password=password)
            return result

    def register(self, username, email, department, password):
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        # validate username
        if not username:
            return Result(False, "Username required!", "username")

        # validate email
        if not email:
            return Result(False, "Email required!", "email")

        if len(email) > 254:
            return Result(False, "Email to large!", "email")

        if not re.match(email_pattern, email):
            return Result(False, "Invalid email format!", "email")

        # validate department
        if not department:
            return Result(False, "Department not selected", "department")

        if not password:
            return Result(False, "Password required!", "password")

        result = self.db.create_user(
            username=username, email=email, department=department, password=password
        )

        return result

    def get_user(self, username):
        result = self.db.get_user(username=username)
        return result
