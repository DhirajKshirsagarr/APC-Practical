
import matplotlib.pyplot as plt

students = ["Rehan", "Arshad", "Varad", "Shiva", "Rohit"]
marks = [70, 85, 90, 65, 80]

plt.barh(students, marks)

plt.title("Student Marks - Horizontal Bar Graph")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()
