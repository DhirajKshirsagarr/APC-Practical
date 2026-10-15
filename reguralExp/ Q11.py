import re

s = input("Enter mobile number: ")
print("Valid" if re.fullmatch(r'[6-9]\d{9}', s) else "Invalid")