import re

s = input("Enter password: ")
p = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'
print("Valid" if re.fullmatch(p, s) else "Invalid")