import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc

from conf.db import session
from conf.models import Teacher, Student, Subject, Group, Grade
from seeds.bd_constants import GROUPS, TEACHERS, STUDENTS, GRADES, SUBJECTS

fake = Faker('uk-UA')


def create_teachers(teachers=1):
    for _ in range(teachers):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(teacher)


def create_group(groups=1):
    last_row_id = session.query(Group.id).order_by(desc(Group.id)).first()
    if last_row_id is None:
        last_row_id = 0
    else:
        last_row_id = last_row_id[0]
    for numb in range(last_row_id, last_row_id + groups):
        group = Group(
            name=f"Group - {numb + 1}"
        )
        session.add(group)


def create_students(students=1):
    groups = session.query(Group).all()
    for _ in range(students):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group_id=random.choice(groups).id
        )
        session.add(student)


def create_subjects(subjects: list):
    teachers = session.query(Teacher).all()
    for subj_ in subjects:
        subject = Subject(
            name=subj_,
            teacher_id=random.choice(teachers).id
        )
        session.add(subject)


def create_grades(grades=1):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for student in students:
        for _ in range(grades):
            grade_ = Grade(
                grade=random.randint(50, 100),
                grade_date=fake.date_this_year(),
                student_id=student.id,
                subjects_id=random.choice(subjects).id

            )
            session.add(grade_)


if __name__ == '__main__':
    try:
        create_group(GROUPS)
        create_teachers(TEACHERS)
        session.commit()

        create_students(STUDENTS)
        create_subjects(SUBJECTS)
        session.commit()

        create_grades(GRADES)
        session.commit()

    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()

