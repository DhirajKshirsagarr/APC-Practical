from student_pkg import marks, grade, attendance

marks_list = [85, 90, 78]
total_marks = marks.total(marks_list)
percent = marks.percentage(marks_list, 300)
student_grade = grade.calculate_grade(percent)
eligible = attendance.is_eligible(80, 100)

print("Total marks =", total_marks)
print("Percentage =", percent)
print("Grade =", student_grade)
print("Attendance eligible:", eligible)