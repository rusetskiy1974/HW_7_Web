GROUPS = 3 #['Група 1', 'Група 2', 'Група 3']
TEACHERS = 4
STUDENTS = 30
SUBJECTS = ['Математика', 'Фізика', 'Хімія', 'Інформатика', 'Англійська', 'Історія', 'Біологія', 'Архітектура БД']
GRADES = 20

STRUCTURE_BD = {
    "groups": [{
        "id": "INTEGER PRIMARY KEY",
        "name": "varchar(100) NOT NULL",
    }, []],
    "teachers": [{
        "id": "INTEGER PRIMARY KEY",
        "fullname": "varchar(150) NOT NULL",
    }, []],
    "subjects": [{
        "id": "INTEGER PRIMARY KEY",
        "name": "varchar(150) NOT NULL",
        "teacher_id_fn": "INTEGER"
    }, ["FOREIGN KEY(teacher_id_fn) REFERENCES teachers(id) on delete cascade"]],
    "students": [{
        "id": "INTEGER PRIMARY KEY",
        "fullname": "varchar(150) NOT NULL",
        "group_id_fn": "INTEGER"
    }, ["FOREIGN KEY(group_id_fn) REFERENCES groups(id) on delete cascade"]],
    "grades": [{
        "id": "INTEGER PRIMARY KEY",
        "grade": "INTEGER CHECK (grade >= 0 AND grade <= 100)",
        "grade_date": "DATE NOT NULL",
        "student_id_fn": "INTEGER",
        "subject_id_fn": "INTEGER"
    }, ["FOREIGN KEY(student_id_fn) REFERENCES students(id) on delete cascade",
        "FOREIGN KEY(subject_id_fn) REFERENCES subjects(id) on delete cascade"]]

}

SAMPLES_FROM_BD = '''
    0. Вихід.
    1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2. Знайти студента із найвищим середнім балом з певного предмета.
    3. Знайти середній бал у групах з певного предмета.
    4. Знайти середній бал на потоці (по всій таблиці оцінок).
    5. Знайти які курси читає певний викладач.
    6. Знайти список студентів у певній групі.
    7. Знайти оцінки студентів у окремій групі з певного предмета.
    8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9. Знайти список курсів, які відвідує студент.
    10. Список курсів, які певному студенту читає певний викладач.
    11. Cередній бал, який певний викладач ставить певному студентові.
    12. Оцінки студентів у певній групі з певного предмета на останньому занятті.'''
