import pytest
from db import SessionLocal
from models import Student


@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()


def test_create_student(db_session):
    student = Student(
        user_id=11111,
        subject_id=1,
        level="Intermediate",
        education_form="personal"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    assert student.user_id is not None
    assert student.level == "Intermediate"

    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session):
    student = Student(
        user_id=22222,
        subject_id=1,
        level="Beginner",
        education_form="group"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student.level = "Advanced"
    db_session.commit()
    db_session.refresh(student)

    assert student.level == "Advanced"

    db_session.delete(student)
    db_session.commit()


def test_delete_student(db_session):
    student = Student(
        user_id=33333,
        subject_id=1,
        level="TestLevel",
        education_form="personal"
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student_user_id = student.user_id

    db_session.delete(student)
    db_session.commit()

    deleted = db_session.query(Student).filter_by(user_id=student_user_id).first()
    assert deleted is None
