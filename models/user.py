import datetime
from zoneinfo import ZoneInfo


class User:
    ALLOWED_ROLES = ("student", "teacher", "admin")

    def __init__(self, first_name, last_name, email, password, role):
        if len(first_name.strip()) < 3:
            raise ValueError("Erro no campo Nome: permitido no mínimo 3 caracteres.")
        if len(first_name.strip()) > 50:
            raise ValueError("Erro no campo Nome: permitido no máximo 50 caracteres.")

        if len(last_name.strip()) < 3:
            raise ValueError("Erro no campo Sobrenome: permitido no mínimo 3 caracteres.")
        if len(last_name.strip()) > 50:
            raise ValueError("Erro no campo Sobrenome: permitido no máximo 50 caracteres.")


        if "@" not in email:
            raise ValueError("E-mail inválido.")
        if "." not in email.split("@")[1]:
            raise ValueError("E-mail inválido.")

        if len(password) < 8:
            raise ValueError("A senha precisa ter no mínimo 8 caracteres.")

        if role not in User.ALLOWED_ROLES:
            raise ValueError("Cargo inválido.")

        self.id = None
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.email = email.lower()
        self._password = password
        self.role = role
        self.is_active = True
        self.created_at = datetime.datetime.now(ZoneInfo("America/Sao_Paulo"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User(id={self.id!r}, email={self.email!r}, role={self.role!r})"