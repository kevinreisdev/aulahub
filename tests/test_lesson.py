from models.lesson import Lesson
import pytest

def test_lesson_filled():
    lesson = Lesson(1, "Lição de preparação", "https://youtube.com.br", 1, 12)

    assert lesson.course_id == 1
    assert lesson.title == "Lição de preparação"
    assert lesson.video_url == "https://youtube.com.br"
    assert lesson.position == 1
    assert lesson.duration_minutes == 12


def test_lesson_title_empty():
    with pytest.raises(ValueError):
        Lesson(1, "", "https://youtube.com.br", 1, 12)


def test_lesson_title_white_space_in_border():
    lesson = Lesson(1, "   Teste   ", "https://youtube.com.br", 1, 12)

    assert lesson.title == "Teste"


def test_lesson_video_url_https_missing_slash():
    with pytest.raises(ValueError):
        Lesson(1, "Teste", "https:/youtube.com.br", 1, 12)


def test_lesson_position_0():
    with pytest.raises(ValueError):
        Lesson(1, "Teste", "https://youtube.com.br", 0, 12)


def test_lesson_position_negative():
    with pytest.raises(ValueError):
        Lesson(1, "Teste", "https://youtube.com.br", -1, 12)


def test_lesson_duration_0():
    with pytest.raises(ValueError):
        Lesson(1, "Teste", "https://youtube.com.br", 2, 0)


def test_title_length_100():
    a = "a" * 100
    lesson = Lesson(1, a, "https://youtube.com.br", 1, 12)

    assert len(lesson.title) == 100


def test_title_length_101():
    a = "a" * 101
    with pytest.raises(ValueError):
        Lesson(1, a, "https://youtube.com.br", 2, 2)


def test_url_https_valid():
    lesson = Lesson(1, "teste", "https://youtube.com.br", 1, 12)

    assert lesson.video_url == "https://youtube.com.br"


def test_url_http_valid():
    lesson = Lesson(1, "teste", "http://youtube.com.br", 1, 12)

    assert lesson.video_url == "http://youtube.com.br"


def test_url_https_center():
    with pytest.raises(ValueError):
        Lesson(1, "teste", "www.https://youtube.com.br", 2, 2)


def test_url_http_center():
    with pytest.raises(ValueError):
        Lesson(1, "teste", "www.http://youtube.com.br", 2, 2)


def test_title_only_spaces():
    with pytest.raises(ValueError):
        Lesson(1, "       ", "https://youtube.com.br", 2, 2)


def test_position_1():
    lesson = Lesson(1, "teste", "https://youtube.com.br", 1, 12)

    assert lesson.position == 1


def test_duration_minutes_1():
    lesson = Lesson(1, "teste", "https://youtube.com.br", 1, 1)

    assert lesson.duration_minutes == 1


def test_url_without_protocol():
    with pytest.raises(ValueError):
        Lesson(1, "teste", "youtube.com.br", 1, 2)