from models.enrollment import Enrollment
import pytest

def test_enrollment_filled():
    enrollment = Enrollment(1, 5, "active")

    assert enrollment.student_id == 1
    assert enrollment.course_id == 5
    assert enrollment.status == "active"


@pytest.mark.parametrize("status", ["active", "completed", "cancelled"])
def test_enrollment_valid_status(status):
    enrollment = Enrollment(1, 5, status)

    assert enrollment.status == status


@pytest.mark.parametrize("status", ["finished", "", "COMPLETED"])
def test_enrollment_invalid_status(status):
    with pytest.raises(ValueError):
        Enrollment(1, 5, status)


def test_enrollment_default_status():
    enrollment = Enrollment(1, 5)

    assert enrollment.status == "active"


def test_enrollment_at_is_set():
    enrollment = Enrollment(1, 5)

    assert enrollment.enrolled_at is not None


def test_enrollment_id_none():
    enrollment = Enrollment(1, 5, "active")

    assert enrollment.id is None