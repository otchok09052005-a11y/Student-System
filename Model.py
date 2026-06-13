
import json
import os

class Student:
    def __init__(self, student_id, name, age):
        self.id = student_id
        self.name = name
        self.age = age

class StudentModel:
    FILE_NAME = "students.json"

    def __init__(self):
        self.students = []
        self.load_students()

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def get_all_students(self):
        return self.students

    def find_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def delete_student(self, student):
        self.students.remove(student)
        self.save_students()

    def load_students(self):
        if not os.path.exists(self.FILE_NAME):
            self.students = []
            return
        try:
            with open(self.FILE_NAME, "r") as file:
                content = file.read().strip()
                if not content:
                    self.students = []
                    return
                data = json.loads(content)
                self.students = [
                    Student(item["id"], item["name"], int(item["age"]))
                    for item in data
                ]
        except (json.JSONDecodeError, KeyError, ValueError):
            self.students = []

    def save_students(self):
        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump(
                    [{"id": s.id, "name": s.name, "age": s.age} for s in self.students],
                    file, indent=4
                )
        except IOError:
            print("Error: Could not save data.")

    def get_statistics(self):
        if not self.students:
            return None
        ages = [s.age for s in self.students]
        return {
            "total": len(self.students),
            "average_age": round(sum(ages) / len(ages), 1),
            "max_age": max(ages),
            "min_age": min(ages)
        }