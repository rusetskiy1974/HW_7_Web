from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = (session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2)
                            .label('average_grade'))
              .select_from(Student)
              .join(Grade)
              .group_by(Student.id)
              .order_by(desc('average_grade'))
              .limit(5).all())
    return result


def select_02():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = (session.query(Student.id, Student.fullname, Subject.name, func.round(func.avg(Grade.grade), 2)
                            .label('average_grade'))
              .select_from(Grade)
              .join(Student)
              .join(Subject)
              .filter(Grade.subjects_id == 1)
              .group_by(Student.id, Subject.name)
              .order_by(desc('average_grade'))
              .limit(1)
              .all())
    return result


def select_03():
    """
    SELECT groups.name AS group_name, subjects.name AS subject, ROUND(AVG(grades.grade), 2) AS average_grade
    FROM groups
    JOIN students ON groups.id = students.group_id_fn
    JOIN grades ON students.id = grades.student_id_fn
    JOIN subjects ON grades.subject_id_fn = subjects.id
    WHERE subjects.id = 2
    GROUP BY groups.name
    ORDER BY average_grade DESC;
    """

    result = ((
        session.query(Group.name, Subject.name, func.round(func.avg(Grade.grade), 2).label('average_grade'))
        .select_from(Group)
        .join(Student)
        .join(Grade)
        .join(Subject)
        .filter(Subject.id == 2)
        .group_by(Group.name, Subject.name)
        .order_by(desc('average_grade')))
        .all())
    return result


def select_04():
    """
    SELECT ROUND(AVG(grade),2) AS average_grade
    FROM grades;
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')).select_from(Grade).all()
    return result


def select_05():
    """
    SELECT teachers.fullname AS name, subjects.name AS subject_name
    FROM subjects
    JOIN teachers ON subjects.teacher_id_fn = teachers.id
    WHERE teachers.id = 3;
    """
    result = (session.query(Teacher.fullname, Subject.name)
              .select_from(Subject)
              .join(Teacher)
              .filter(Teacher.id == 4)
              .all())
    return result


def select_06():
    """
    SELECT groups.name AS group_name,  students.fullname AS student_name
    FROM students
    JOIN groups ON students.group_id_fn  = groups.id
    WHERE groups.id = 2;
    """
    result = (session.query(Group.name, Student.fullname)
              .select_from(Student)
              .join(Group)
              .filter(Group.id == 2)
              .all())
    return result


def select_07():
    """
    SELECT s.fullname AS student_name, groups.name, subjects.name, grades.grade, grades.grade_date
    FROM students s
    JOIN groups ON s.group_id_fn = groups.id
    JOIN grades ON s.id = grades.student_id_fn
    JOIN subjects ON grades.subject_id_fn  = subjects.id
    WHERE groups.id = 1 AND subjects.id = 2;
    """
    result = (session.query(Student.fullname, Group.name, Subject.name, Grade.grade, Grade.grade_date)
              .select_from(Student)
              .join(Group)
              .join(Grade)
              .join(Subject)
              .filter(and_(Group.id == 1, Subject.id == 2))
              .order_by(Student.fullname)
              .all())
    return result


def select_08():
    """
    SELECT teachers.fullname AS teacher_name, subjects.name AS subject_name, ROUND(AVG(grades.grade), 2) AS average_grade
    FROM teachers
    JOIN subjects ON teachers.id = subjects.teacher_id_fn
    JOIN grades ON subjects.id = grades.subject_id_fn
    WHERE  teachers.id = 1
    GROUP BY teacher_name, subject_name;
    """

    result = (session.query(Teacher.fullname, Subject.name, func.round(func.avg(Grade.grade), 2))
              .select_from(Teacher)
              .join(Subject)
              .join(Grade)
              .filter(Teacher.id == 2)
              .group_by(Teacher.fullname, Subject.name)
              .all())

    return result


def select_09():
    """
    SELECT students.fullname AS name, subjects.name AS  subject_name, grades.grade_date AS data
    FROM students
    JOIN grades ON students.id = grades.student_id_fn
    JOIN subjects ON grades.subject_id_fn  = subjects.id
    WHERE students.id = 6
    ORDER BY data ;
    """

    result = (session.query(Student.fullname, Subject.name)
              .select_from(Student)
              .join(Grade)
              .join(Subject)
              .filter(Student.id == 6)
              .order_by(Subject.name)
              .distinct(Subject.name)
              .all())
    return result


def select_10():
    """
    SELECT s.fullname AS name, subjects.name AS subject_name, t.fullname AS teacher_name, g.grade_date AS data
    FROM students s
    JOIN grades g ON s.id = g.student_id_fn
    JOIN subjects ON g.subject_id_fn = subjects.id
    JOIN teachers t ON subjects.teacher_id_fn  = t.id
    WHERE s.id = 20 AND t.id = 3
    ORDER BY data;
    """
    result = (session.query(Subject.name, Student.fullname, Teacher.fullname)
              .select_from(Student)
              .join(Grade)
              .join(Subject)
              .join(Teacher)
              .filter(and_(Student.id == 20, Teacher.id == 2))
              .order_by(Subject.name)
              .distinct(Subject.name)
              .all())

    return result


def select_11():
    """
    SELECT s.fullname AS name, ROUND(AVG(g.grade),2 ) AS average_grade, t.fullname AS teacher_name
    FROM students s
    JOIN grades g ON s.id = g.student_id_fn
    JOIN subjects ON g.subject_id_fn = subjects.id
    JOIN teachers t ON subjects.teacher_id_fn = t.id
    WHERE s.id = 8 AND t.id = 3;
    """
    result = (session.query(Student.fullname, Teacher.fullname, func.round(func.avg(Grade.grade), 2))
              .select_from(Student)
              .join(Grade)
              .join(Subject)
              .join(Teacher)
              .filter(and_(Student.id == 10, Teacher.id == 3))
              .group_by(Student.fullname, Teacher.fullname)
              .all())

    return result


def select_12():
    """
    SELECT groups.name AS group_name, s.fullname AS student_name, grades.grade, grades.grade_date
    FROM students s
    JOIN groups ON s.group_id_fn = groups.id
    JOIN grades  ON s.id = grades.student_id_fn
    JOIN subjects ON grades.subject_id_fn = subjects.id
    WHERE groups.id = 2
    AND subjects.id = 2
    AND grades.grade_date = (
        SELECT MAX(grade_date)
        FROM grades
        WHERE subject_id_fn = subjects.id
);
    """
    result = (session.query(Group.name, Student.fullname, Subject.name, Grade.grade, Grade.grade_date)
              .select_from(Student)
              .join(Group)
              .join(Grade)
              .join(Subject)
              .filter(and_(Group.id == 2, Subject.id == 2, Grade.grade_date == (select(func.max(Grade.grade_date))
                                                                                .filter(Grade.subjects_id == 2)
                                                                                .scalar_subquery())))
              .all())

    return result


if __name__ == '__main__':
    print('1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.')
    [print(el) for el in select_01()]
    print('\n2. Знайти студента із найвищим середнім балом з певного предмета.')
    [print(el) for el in select_02()]
    print('\n3. Знайти середній бал у групах з певного предмета.')
    [print(el) for el in select_03()]
    print('\n4. Знайти середній бал на потоці (по всій таблиці оцінок).')
    [print(el) for el in select_04()]
    print('\n5. Знайти які курси читає певний викладач.')
    [print(el) for el in select_05()]
    print('\n6. Знайти список студентів у певній групі.')
    [print(el) for el in select_06()]
    print('\n7. Знайти оцінки студентів у окремій групі з певного предмета.')
    [print(el) for el in select_07()]
    print('\n8. Знайти середній бал, який ставить певний викладач зі своїх предметів.')
    [print(el) for el in select_08()]
    print('\n9. Знайти список курсів, які відвідує студент.')
    [print(el) for el in select_09()]
    print('\n10. Список курсів, які певному студенту читає певний викладач.')
    [print(el) for el in select_10()]
    print('\n11. Cередній бал, який певний викладач ставить певному студентові.')
    [print(el) for el in select_11()]
    print('\n12. Оцінки студентів у певній групі з певного предмета на останньому занятті.')
    [print(el) for el in select_12()]
