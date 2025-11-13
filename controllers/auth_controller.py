from db.database import Database


class AuthController:
    def __init__(self):
        self.db = Database()

    def login(self, username, password):
        result = self.db.verify_user(username=username, password=password)
        return result

    def register(self, username, email, department, password):
        result = self.db.create_user(
            username=username, email=email, department=department, password=password
        )
        return result

    def get_user(self, username):
        result = self.db.get_user(username=username)
        return result
