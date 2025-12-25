import sqlite3


def create_db():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # 2️⃣ Создание таблиц (Студенты и Оценки)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            hobby TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT NOT NULL,
            score INTEGER CHECK(score >= 1 AND score <= 100),
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')

    # 👁 Создание VIEW
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS student_report AS
        SELECT s.full_name, g.subject, g.score
        FROM students s
        LEFT JOIN grades g ON s.id = g.student_id
    ''')

    conn.commit()
    conn.close()


# ✅ Функции добавления данных
def add_student(name, hobby):
    with sqlite3.connect('school.db') as conn:
        conn.execute("INSERT INTO students (full_name, hobby) VALUES (?, ?)", (name, hobby))


def add_grade(student_id, subject, score):
    with sqlite3.connect('school.db') as conn:
        conn.execute("INSERT INTO grades (student_id, subject, score) VALUES (?, ?, ?)",
                     (student_id, subject, score))


# 📖 JOIN-запрос
def get_all_info():
    print("\n--- Полный список (LEFT JOIN) ---")
    with sqlite3.connect('school.db') as conn:
        cursor = conn.execute('''
            SELECT s.full_name, g.subject, g.score 
            FROM students s
            LEFT JOIN grades g ON s.id = g.student_id
        ''')
        for row in cursor.fetchall():
            print(f"Студент: {row[0]} | Предмет: {row[1] or 'Нет данных'} | Оценка: {row[2] or '-'}")


# 📊 Агрегатные функции (AVG, MAX, SUM)
def show_statistics():
    print("\n--- Статистика успеваемости ---")
    with sqlite3.connect('school.db') as conn:
        cursor = conn.execute('''
            SELECT AVG(score), MAX(score), SUM(score) FROM grades
        ''')
        res = cursor.fetchone()
        print(f"Средний балл: {res[0]:.2f} | Макс. балл: {res[1]} | Сумма всех баллов: {res[2]}")


# 🔍 GROUP BY
def count_grades_per_student():
    print("\n--- Количество оценок у каждого студента (GROUP BY) ---")
    with sqlite3.connect('school.db') as conn:
        cursor = conn.execute('''
            SELECT s.full_name, COUNT(g.id)
            FROM students s
            LEFT JOIN grades g ON s.id = g.student_id
            GROUP BY s.full_name
        ''')
        for row in cursor.fetchall():
            print(f"Студент: {row[0]} | Оценок получено: {row[1]}")


# 👀 Подзапрос (SUBQUERY)
def find_excellent_students():
    print("\n--- Студенты, у которых есть оценка выше 90 (SUBQUERY) ---")
    with sqlite3.connect('school.db') as conn:
        cursor = conn.execute('''
            SELECT full_name FROM students 
            WHERE id IN (SELECT student_id FROM grades WHERE score > 90)
        ''')
        for row in cursor.fetchall():
            print(f"Отличник: {row[0]}")


# 👁 Функция чтения из VIEW
def read_view():
    print("\n--- Данные из VIEW (Представление) ---")
    with sqlite3.connect('school.db') as conn:
        cursor = conn.execute("SELECT * FROM student_report")
        for row in cursor.fetchall():
            print(f"VIEW -> {row[0]} | {row[1]}: {row[2]}")


# Основной блок запуска
if __name__ == "__main__":
    create_db()


    add_student("Иван Иванов", "Программирование")
    add_student("Анна Смирнова", "Рисование")

    add_grade(1, "Python", 95)
    add_grade(1, "Math", 88)
    add_grade(2, "Art", 100)


    get_all_info()
    show_statistics()
    count_grades_per_student()
    find_excellent_students()
    read_view()
