class Student:
    """"Определение атребутов класса Student"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()

    def rate_hw(self, lecturer, course, grade):
        """"Определение метода высталения оценок экземплярам класса Lecturer"""
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Перегрузка магического метода __str__ в формате:
        print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за домашние задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Введение в программирование
        """

        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_grade = round(sum(map(sum, self.grades.values())) / grades_count, 2)
        result = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_grade}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return result

    def __lt__(self, other):
        """Реализует возможность сравнивать (через операторы сравнения)
        между собой студентов по средней оценке за домашние задания."""
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grade < other.average_grade


class Mentor:
    """"Определение атребутов класса Mentor"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        """"Наследование атребутов класса Lecturer от класса Mentor"""
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = float()

    def __str__(self):
        """"Перегрузка магического метода __str__ у класса Lecturer. В формате:
            pprint(some_lecturer)
            Имя: Some
            Фамилия: Buddy
            Средняя оценка за лекции: 9.9"""
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_grade = round(sum(map(sum, self.grades.values())) / grades_count, 2)
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return result

    def __lt__(self, other):
        """Реализация возможности сравнивать (через операторы сравнения)
        между собой лекторов по средней оценке за лекции. """
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_grade < other.average_grade

class Reviewer(Mentor):
    """"Наследование атребутов класса Reviewer от класса Mentor"""
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        """"Определение метода высталения оценок экземплярам класса Student"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """"Перегрузка магического метода __str__ у класса Reviewer. В формате:
            print(some_reviewer)
            Имя: Some
            Фамилия: Buddy"""
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

# Создаем лекторов и закрепляем их за курсом
cool_lecturer_1 = Lecturer('Ivan', 'Ivanov')
cool_lecturer_1.courses_attached += ['Python']

cool_lecturer_2 = Lecturer('Petr', 'Petrov')
cool_lecturer_2.courses_attached += ['Java']

# Создаем проверяющих и закрепляем их за курсом
cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('One', 'Person')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
best_student_1 = Student('Sergey', 'Molchanov', 'your_gender')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ['Введение в программирование']

best_student_2 = Student('Ruoy', 'Eman', 'your_gender')
best_student_2.courses_in_progress += ['Java']
best_student_2.finished_courses += ['Введение в программирование']

# Выставляем оценки лекторам за лекции
best_student_1.rate_hw(cool_lecturer_1, 'Python', 10)
best_student_1.rate_hw(cool_lecturer_1, 'Python', 10)
best_student_1.rate_hw(cool_lecturer_1, 'Python', 10)

best_student_1.rate_hw(cool_lecturer_2, 'Java', 9)
best_student_1.rate_hw(cool_lecturer_2, 'Java', 9)
best_student_1.rate_hw(cool_lecturer_2, 'Java', 10)

best_student_2.rate_hw(cool_lecturer_1, 'Python', 10)
best_student_2.rate_hw(cool_lecturer_1, 'Python', 9)
best_student_2.rate_hw(cool_lecturer_1, 'Python', 9)

best_student_2.rate_hw(cool_lecturer_2, 'Java', 10)
best_student_2.rate_hw(cool_lecturer_2, 'Java', 10)
best_student_2.rate_hw(cool_lecturer_2, 'Java', 10)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)

cool_reviewer_2.rate_hw(best_student_2, 'Java', 10)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 9)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 9)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Список студентов:\n\n{best_student_1}\n\n{best_student_2}')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Список лекторов:\n\n{cool_lecturer_1}\n\n{cool_lecturer_2}')
print()
print()

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{best_student_1.name} {best_student_1.surname} < {best_student_2.name} {best_student_2.surname} = {best_student_1 > best_student_2}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{cool_lecturer_1.name} {cool_lecturer_1.surname} < {cool_lecturer_2.name} {cool_lecturer_2.surname} = {cool_lecturer_1 > cool_lecturer_2}')
print()

# Создаем список студентов
student_list = [best_student_1, best_student_2]

# Создаем список лекторов
lecturer_list = [cool_lecturer_1, cool_lecturer_2]

#

def average_grade_student(student_list, course_name):
    """Функция для для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса);"""

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_grade
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

def average_grade_lecturer(lecturer_list, course_name):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    (в качестве аргумента принимаем список лекторов и название курса)"""

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_grade
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {average_grade_student(student_list, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {average_grade_lecturer(lecturer_list, 'Python')}")
print()






