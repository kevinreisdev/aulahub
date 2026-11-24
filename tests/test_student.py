from models.student import Student
from models.user import User
import pytest


def test_student_role():
    user = Student("Kevin", "Reis", "kevin@gmail.com", "12345678")

    assert user.role == "student"


def test_student_role_isinstance():
    user = Student("Kevin", "Reis", "kevin@gmail.com", "12345678")

    assert isinstance(user, User)


def test_too_short_password():
    with pytest.raises(ValueError):
        Student("Kevin", "Reis", "kevin@gmail.com", "1234567")