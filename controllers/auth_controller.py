class AuthController:

    def login(self, username, password):

        if username and password:
            return True
        return False
