# Studenten Class
class Student:
    students = None
    no_of_student = 0
    all_students = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course = []
        Student.no_of_student += 1
        Student.all_students.append(self)

    # fügt einen Kurs zur Liste der vom Studenten besuchten Kurse hinzu.
    def enroll(self, *courses):
        for course in courses:
            if course not in self.course:
                self.course.append(course)
            else:
                print("Dieses Kurs existiert bereits")

    def details(self):
        return f"Student Name: {self.name}, Age: {self.age}, Courses: {self.course}"

    @classmethod
    def get_course_participants(cls, course):
        participants = []
        for student in Student.all_students:
            if course in student.course:
                participants.append(student.__str__())
        return participants

    @classmethod
    def get_no_of_students(cls):
        return cls.no_of_student

    def __str__(self):
        return self.details()

    @classmethod
    def get_all_students(cls):
        student_details = [student.__str__() for student in cls.all_students]
        return "\n".join(student_details) + "\n"





s1 = Student("Taha", 25)
s2 = Student("Ali", 23)
s3 = Student("Max", 23)
s1.enroll("Programmierung", "Datenbanken", "TI", "Mathe")
s2.enroll("Python", "Datenbanken", "TI", "Mathe")
s3.enroll("Algebra", "Datenbanken", "TI", "Python")
print(Student.get_course_participants("Python"))

"""

s2.course = ["TI", "Datenbanken"]
s3.course = ["TI", "Programmierung"]

print(s1)
print(s2)
print(s3)
print()
print(Student.get_all_students())
print()
print(repr(Student.get_course_participants("Datenbanken")))
"""
