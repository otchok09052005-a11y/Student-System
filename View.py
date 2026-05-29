class StudentView:

    def display_menu(self):
        print("\n===== STUDENT INFORMATION SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

    def show_students(self, students):
        print("\n--- Student List ---")
        if not students:
            print("No students found.")
            return

        for i, s in enumerate(students, start=1):
            print(f"{i}. ID: {s.id}, Name: {s.name}, Age: {s.age}")

    def show_message(self, message):
        print(message)

    def input_id(self):
        return input("Enter Student ID (numbers only): ")

    def input_name(self):
        return input("Enter Student Name: ")

    def input_age(self):
        return input("Enter Age: ")
