class Student:
    def __init__(self, student_id, name, age):
        self.id = student_id
        self.name = name
        self.age = age


class StudentModel:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return self.students

    def find_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def delete_student(self, student):
        self.students.remove(student)