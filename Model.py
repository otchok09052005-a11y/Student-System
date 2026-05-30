import json
FILE_NAME = "students.json"

def load_students(self):
    try:
        with open(self.FILE_NAME, "r") as file:
            data = json.load(file)
            self.students = [Student(s["id"], s["name"], s["age"]) for s in data]
    except FileNotFoundError:
        self.students = []

        def save_students(self):
    with open(self.FILE_NAME, "w") as file:
        json.dump(
            [{"id": s.id, "name": s.name, "age": s.age} for s in self.students],
            file,
            indent=4
        )
        

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