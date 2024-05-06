from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    result = (
        session.query(
            Student.id,
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .select_from(Student)
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("average_grade"))
        .limit(5)
        .all()
    )
    return result


def select_02():
    result = (
        session.query(
            Student.id,
            Student.fullname,
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .filter(Grade.subject_id == 3)
        .group_by(Student.id)
        .order_by(desc("average_grade"))
        .limit(1)
        .all()
    )
    return result


def select_03():
    result = (
        session.query(
            Group.fullname, func.round(func.avg(Grade.grade), 2).label("average_grade")
        )
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(Grade.subject_id == 1)
        .group_by(Group.id)
        .all()
    )
    return result


def select_04():
    result = (
        session.query(func.round(func.avg(Grade.grade), 2).label("average_grade"))
        .select_from(Grade)
        .limit(1)
        .all()
    )
    return result


def select_05():
    result = (
        session.query(Subject.id, Subject.fullname, Teacher.fullname)
        .select_from(Subject)
        .join(Teacher)
        .filter(Subject.teacher_id == 1)
        .all()
    )
    return result


def select_06():
    result = (
        session.query(Student.id, Student.fullname, Group.fullname)
        .select_from(Student)
        .join(Group)
        .filter(Student.group_id == 1)
        .all()
    )
    return result


def select_07():
    result = (
        session.query(Group.fullname, Subject.fullname, Grade.grade, Student.fullname)
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(and_(Grade.subject_id == 1, (Group.id == 1)))
        .all()
    )
    return result


def select_08():
    result = (
        session.query(
            Teacher.fullname,
            Subject.fullname,
            func.round(func.avg(Grade.grade), 2).label("average_grade"),
        )
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Teacher)
        .filter(Subject.teacher_id == 1)
        .group_by(Subject.id, Teacher.fullname, Subject.fullname)
        .all()
    )
    return result


def select_09():
    result = (
        session.query(Student.fullname, Subject.fullname)
        .select_from(Subject)
        .join(Grade)
        .join(Student)
        .filter(Grade.student_id == 5)
        .group_by(Subject.id, Student.fullname, Subject.fullname)
        .all()
    )
    return result


def select_10():
    result = (
        session.query(Teacher.fullname, Subject.fullname, Student.fullname)
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Teacher)
        .filter(and_(Grade.student_id == 1, (Teacher.id == 1)))
        .group_by(
            Subject.id, Student.fullname, Subject.fullname, Teacher.id, Teacher.fullname
        )
        .all()
    )
    return result


if __name__ == "__main__":
    # print(select_01())
    # print(select_02())
    # print(select_03())
    # print(select_04())
    # print(select_05())
    # print(select_06())
    # print(select_07())
    # print(select_08())
    # print(select_09())
    print(select_10())
