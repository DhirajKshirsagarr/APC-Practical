class Faculty:
    def __init__(self, faculty_id, name, department):
        self.faculty_id = faculty_id
        self.name = name
        self.department = department

    def get_details(self):
        return f"Faculty ID: {self.faculty_id} Name: {self.name}  Department: {self.department}"
