from Model import StudentModel
from View import StudentView
from Controller import StudentController

if __name__ == "__main__":
    app_model = StudentModel()
    app_view = StudentView()
    app_controller = StudentController(app_model, app_view)
    app_view.mainloop()