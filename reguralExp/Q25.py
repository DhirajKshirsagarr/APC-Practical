import re

s = input("Enter student details: ")

p = r'Name:\s*(\w+)\s*,\s*Roll:\s*(\d+)\s*,\s*Marks:\s*(\d+)'
result = re.findall(p, s)

for name, roll, marks in result:
    print("Name:", name, "Roll:", roll, "Marks:", marks)