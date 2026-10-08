class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

    def get_details(self):
        return f"Student ID: {self.student_id} Name: {self.name} Major: {self.major}"
