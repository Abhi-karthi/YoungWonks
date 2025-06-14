import random
class Person:
    def __init__(self, first, last, email, DOB):
        self.first = first
        self.last = last
        self.email = email
        self.DOB = DOB


class Teacher(Person):
    def __init__(self, class_number, subject, first, last, email, DOB, students: list):
        super().__init__(first, last, email, DOB)
        self.class_number = class_number
        self.subject = subject
        self.students = students


class Student(Person):
    def __init__(self, student_id, grade, first, last, email, DOB):
        Person.__init__(self, first, last, email, DOB)
        self.student_id = student_id
        self.grade = grade


students = [Student(12345, 6, "abc", "def", "ghi@gmail.com", "7/7/2007"), Student(123457, 7, "dbc", "aef", "gli@gmail.com", "7/8/2007"), Student(123456, 12, "ljl", "asdf", "uil@gmail.com", "8/7/2007")]
teacher = Teacher(123, "math", "John", "Doe", "teacher@gmail.com", "1/1/1701", [students[0], students[1], students[2]])
a = random.choice(students)
print(teacher.students[0].first)