import re

s = input("Enter product code: ")
p = r'[A-Z]{3}-\d{4}-[A-Z]{2}'

print("Valid" if re.fullmatch(p, s) else "Invalid")