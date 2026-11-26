from datetime import datetime, timezone


class Enrollment:
    STATUS_LIST = ("active", "completed", "cancelled")

    def __init__(self, student_id, course_id, status="active"):
        if status not in Enrollment.STATUS_LIST:
            raise ValueError("Status inválido.")

        self.id = None
        self.student_id = student_id
        self.course_id = course_id
        self.status = status
        self.enrolled_at = datetime.now(timezone.utc)