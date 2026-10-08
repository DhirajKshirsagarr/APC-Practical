class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def get_details(self):
        return f"Course Code: {self.course_code} {self.course_name} {self.credits} Credits"
