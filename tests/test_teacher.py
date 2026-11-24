from models.teacher import Teacher
from models.user import User
import pytest


def test_teacher_role():
    user = Teacher("Kevin", "Reis", "kevin@gmail.com", "12345678")

    assert user.role == "teacher"


def test_max_characters_teacher_bio():
    a = "a" * 501
    with pytest.raises(ValueError):
        Teacher("Kevin", "Reis", "kevin@gmail.com", "12345678", a)


def test_characters_teacher_bio_500():
    a = "a" * 500
    user = Teacher("Kevin", "Reis", "kevin@gmail.com", "12345678", a)

    assert user.bio == a


def test_bio_empty():
    user = Teacher("Kevin", "Reis", "kevin@gmail.com", "12345678")

    assert user.bio == ""


def test_teacher_role_isinstance():
    user = Teacher("Kevin", "Reis", "kevin@gmail.com", "12345678")

    assert isinstance(user, User)


def test_too_short_password():
    with pytest.raises(ValueError):
        Teacher("Kevin", "Reis", "kevin@gmail.com", "1234567")