from datetime import datetime
import random

from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher,Student,Subject,Grade,Group
from faker import Faker

fake_data =Faker()

def insert_groups():
    for _ in range(4):
        group = Group(
            fullname=fake_data.license_plate()
        )
        session.add(group)
def insert_students():
    groups = session.query(Group).all()
    for _ in range(30):
        student = Student(
            fullname=fake_data.name(),
            group_id=random.choice(groups).id
        )
        session.add(student)

def insert_teachers():
    for _ in range(3):
        teacher = Teacher(
            fullname=fake_data.name()
        )
        session.add(teacher)

def insert_subjects():
    teachers = session.query(Teacher).all()
    for _ in range(5):
        subject = Subject(
            fullname = fake_data.job(),
            teacher_id =random.choice(teachers).id
        )
        session.add(subject)


def insert_grades():
    subjects = session.query(Subject).all()
    students = session.query(Student).all()

    for _ in range(600):
        grade = Grade(
            grade = random.randint(0, 100),
            grade_date = fake_data.date_between_dates(date_start=datetime(2023,9,1), date_end=datetime.today()),
            student_id = random.choice(students).id,
            subject_id = random.choice(subjects).id
        )
        session.add(grade)



if __name__ == '__main__':
    try:
        insert_groups()
        session.commit()
        insert_students()
        session.commit()
        insert_teachers()
        session.commit()
        insert_subjects()
        session.commit()
        insert_grades()
        session.commit()


    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
