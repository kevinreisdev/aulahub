import datetime
from zoneinfo import ZoneInfo


class User:
    def __init__(self, first_name, last_name, email, password, role):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email.lower()
        self._password = password
        self.role = role
        self.is_active = True
        self.created_at = datetime.datetime.now(ZoneInfo("America/Sao_Paulo"))