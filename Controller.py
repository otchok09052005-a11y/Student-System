from Model import StudentModel
from View import StudentView


class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

    def run(self):
        while True:
            self.view.display_menu()
            choice = input("Enter choice (1-6): ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                self.view.show_message("Exiting program. Goodbye!")
                break
            else:
                self.view.show_message("Invalid choice!")

    def add_student(self):
        sid = self.view.input_id()
        name = self.view.input_name()
        age = self.view.input_age()

        student= (sid, name, age)
        self.model.add_student(student)

        self.view.show_message("Student added successfully!")

    def view_students(self):
        self.view.show_students(self.model.get_all_students())

    def search_student(self):
        sid = self.view.input_id()
        student = self.model.find_student(sid)

        if student:
            self.view.show_message(
                f"Found: ID: {student.id}, Name: {student.name}, Age: {student.age}"
            )
        else:
            self.view.show_message("Student not found.")

    def update_student(self):
        sid = self.view.input_id()
        student = self.model.find_student(sid)
if student:
    new_name = input(f"New Name ({student.name}): ")
    new_age = input(f"New Age ({student.age}): ")

    if new_name:
        student.name = new_name
    if new_age:
        student.age = new_age
    self.model.save_students()
    self.view.show_message("Student updated successfully!")

    def delete_student(self):
        sid = self.view.input_id()
        student = self.model.find_student(sid)

        if student:
            self.model.delete_student(student)
            self.view.show_message("Student deleted successfully!")
        else:
            self.view.show_message("Student not found.")

if __name__ == "__main__":
    app =  StudentController()
    app.run()
