from datetime import datetime, timezone


class Course:
    def __init__(self, title, teacher_id, description=""):
        if title.strip() == "":
            raise ValueError("O título não pode ficar em branco")
        if len(title.strip()) > 100:
            raise ValueError("O título deve conter no máximo 100 caracteres")
        if len(title.strip()) < 10:
            raise ValueError("O título deve conter no mínimo 10 caracteres")

        self.id = None
        self.title = title.strip()
        self.description = description
        self.teacher_id = teacher_id
        self.is_published = False
        self.created_at = datetime.now(timezone.utc)
