from Model import StudentModel, Student

class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.on_add_click = self.add_student
        self.view.on_delete_click = self.delete_student
        self.view.on_update_click = self.update_student
        self.view.on_stats_click = self.display_stats
        self.view.on_select_record = self.populate_fields_from_selection

        self.view.refresh_directory(self.model.get_all_students())

    def add_student(self):
        sid, name, age_str = self.view.get_inputs()

        if not sid.isdigit() or not name or not age_str.isdigit():
            self.view.show_message("Format Error", "All fields are required. ID and Age must be digits.", is_error=True)
            return

        if self.model.find_student(sid):
            self.view.show_message("Duplicate Record", f"Student with ID {sid} already exists.", is_error=True)
            return

        new_student = Student(sid, name, int(age_str))
        self.model.add_student(new_student)
        
        self.view.refresh_directory(self.model.get_all_students())
        self.view.clear_inputs()
        self.view.show_message("Success", "Student registered successfully.")

    def update_student(self):
        sid, name, age_str = self.view.get_inputs()
        student = self.model.find_student(sid)

        if not student:
            self.view.show_message("Selection Error", "Please select a valid record from the table directory.", is_error=True)
            return

        if name:
            student.name = name
        if age_str and age_str.isdigit():
            student.age = int(age_str)

        self.model.save_students()
        self.view.refresh_directory(self.model.get_all_students())
        self.view.clear_inputs()
        self.view.show_message("Success", "Student record configuration updated.")

    def delete_student(self):
        selected_item = self.view.tree.selection()
        if not selected_item:
            self.view.show_message("Selection Error", "Choose a student record to erase.", is_error=True)
            return

        values = self.view.tree.item(selected_item, "values")
        student = self.model.find_student(values[0])

        if student:
            self.model.delete_student(student)
            self.view.refresh_directory(self.model.get_all_students())
            self.view.clear_inputs()
            self.view.show_message("Success", "Student records cleared safely.")

    def populate_fields_from_selection(self):
        selected_item = self.view.tree.selection()
        if selected_item:
            values = self.view.tree.item(selected_item, "values")
            self.view.set_inputs(values[0], values[1], values[2])

    def display_stats(self):
        stats = self.model.get_statistics()
        if not stats:
            self.view.show_message("Analytics Panel", "Insufficient student volume to compile dashboard metrics.", is_error=True)
            return
            
        summary = (
            f"Total Enrolled: {stats['total']}\n"
            f"Average Age: {stats['average_age']}\n"
            f"Oldest Record: {stats['max_age']}\n"
            f"Youngest Record: {stats['min_age']}"
        )
        self.view.show_message("System Statistics Dashboard", summary)