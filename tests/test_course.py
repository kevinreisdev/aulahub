from models.course import Course
import pytest


def test_course_filled():
    course = Course("Fundamentos de Python 3", 63)

    assert course.title == "Fundamentos de Python 3"
    assert course.teacher_id == 63
    assert course.description == ""
    assert course.is_published == False


def test_course_max_len_title():
    a = "a" * 101
    with pytest.raises(ValueError):
        Course(a, 63)


def test_course_min_len_title():
    a = "a" * 9
    with pytest.raises(ValueError):
        Course(a, 63)


def test_course_empty_title():
    a = ""
    with pytest.raises(ValueError):
        Course(a, 63)


def test_course_limit_len_title():
    a = "a" * 100
    course = Course(a, 63)

    assert len(course.title) == 100


def test_course_white_spaces_in_title():
    with pytest.raises(ValueError):
        Course("                             ", 63)


def test_course_10_characters_title():
    a = "a" * 10
    course = Course(a, 63)

    assert len(course.title) == 10


def test_course_title_with_spaces():
    with pytest.raises(ValueError):
        Course("      Python     ", 63)