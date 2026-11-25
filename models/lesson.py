class Lesson:
    def __init__(self, course_id, title, video_url, position, duration_minutes):
        if title.strip() == "":
            raise ValueError("O título não pode ficar vazio")
        if len(title.strip()) > 100:
            raise ValueError("O título pode conter no máximo 100 caracteres")

        if not video_url.startswith(("https://", "http://")):
            raise ValueError("Link do vídeo inválido")

        if position <= 0:
            raise ValueError("A posição do vídeo deve ser maior que 0")

        if duration_minutes <= 0:
            raise ValueError("A duração do vídeo deve ser maior que 0")

        self.id = None
        self.course_id = course_id
        self.title = title.strip()
        self.video_url = video_url
        self.position = position
        self.duration_minutes = duration_minutes