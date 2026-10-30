import student

marks = [85, 90, 78, 88, 92]
total = student.total_marks(marks)
percent = student.percentage(marks, 500)
grade = student.grade(percent)

print("Total marks =", total)
print("Percentage =", percent)
print("Grade =", grade)