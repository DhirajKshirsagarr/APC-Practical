
from collage.student import Student
from collage.faculty import Faculty
from collage.course import Course

def main():
    student1 = Student("58", "dhiraj Kshirsagar", "Computer Science")
    faculty1 = Faculty("75", "Mrs. shinge", "Advance programing concept")
    course1 = Course("CSExxxxxx", "Advanced Python Programming", 2)

    print(student1.get_details())
    print("\n",faculty1.get_details())
    print("\n",course1.get_details())

if __name__ == "__main__":
    main()
