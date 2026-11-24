import pytest
from models.user import User


def test_create_valid_user():
    user = User("Kevin", "Reis", "kevin@gmail.com", "123456789", "student")

    assert user.first_name == "Kevin"
    assert user.last_name == "Reis"
    assert user.role == "student"
    assert user.is_active is True


# raises test
def test_password_too_short():
    with pytest.raises(ValueError):
        User("Kevin", "Reis", "kevin@gmail.com", "1234567", "student")


def test_name_too_short():
    with pytest.raises(ValueError):
        User("Ke", "Reis", "kevin@gmail.com", "12345678", "student")


def test_first_name_too_long():
    with pytest.raises(ValueError):
        User("vinKevinKevinKevinKevinKevinKevinKevinKevinKevinKevinKevinKevinKevinKevinKevinKe", "Reis", "kevin@gmail.com", "12345678", "student")


def test_role_list():
    with pytest.raises(ValueError):
        User("Kevin", "Reis", "kevin@gmail.com", "12345678", "Teacher")


def test_arroba_email():
    with pytest.raises(ValueError):
        User(" Kevin ", "Reis", "kevingmail.com", "123456789", "student")


# assert tests
def test_return_str_user():
    user = User("Kevin", "Reis", "kevin@gmail.com", "123456789", "student")

    assert str(user) == "Kevin Reis"


def test_create_strip_name():
    user = User(" Kevin ", "  Reis ", "kevin@gmail.com", "123456789", "student")

    assert user.first_name == "Kevin"
    assert user.last_name == "Reis"


def test_first_and_last_name_exactly_3_characters():
    user = User("Kev", "Rei", "kevin@gmail.com", "123456789", "student")

    assert len(user.first_name) == 3
    assert len(user.last_name) == 3



def test_lower_email():
    user = User(" Kevin ", "Reis", "KEVIN@gmail.com", "123456789", "student")

    assert user.email == "kevin@gmail.com"


def test_name_exactly_50():
    user = User("vinKevinKevinKevinKevinKevinKevinKevinKevinKevinKe", "Reis", "kevin@gmail.com", "12345678", "student")

    assert len(user.first_name) == 50


def test_password_exactly_8_characters():
    user = User("Kevin", "Reis", "kevin@gmail.com", "12345678", "student")

    assert user.email == "kevin@gmail.com"


def test_email_without_dot():
    with pytest.raises(ValueError):
        User("Kevin", "Reis", "kevin@gmailcom", "12345678", "student")