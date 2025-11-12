from db.user_model import User


class AuthController:

    def login(self, username, password):
        user_model = User()
        result = user_model.verify_user(username=username, password=password)
        return result

    def register(self, username, email, department, password):
        user_model = User()
        result = user_model.create_user(
            username=username, email=email, department=department, password=password
        )
        return result
