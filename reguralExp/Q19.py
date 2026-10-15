import re

s = input("Enter vehicle number: ")
p = r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}'
print("Valid" if re.fullmatch(p, s) else "Invalid")