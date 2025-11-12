from db.user_model import User


class AuthController:

    def login(self, username, password):

        if username and password:
            return True
        return False

    def register(self, username, email, department, password):
        user_model = User()
        result = user_model.create_user(
            username=username, email=email, department=department, password=password
        )
        return result
