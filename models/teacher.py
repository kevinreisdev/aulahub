from models.user import User


class Teacher(User):
    def __init__(self, first_name, last_name, email, password, bio=""):
        super().__init__(first_name, last_name, email, password, role="teacher")

        if len(bio) > 500:
            raise ValueError("A bio pode ter no máximo 500 caracteres.")

        self.bio = bio