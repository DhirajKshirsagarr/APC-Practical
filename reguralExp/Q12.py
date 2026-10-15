import re

s = input("Enter email: ")
print("Valid" if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w{2,}', s) else "Invalid")