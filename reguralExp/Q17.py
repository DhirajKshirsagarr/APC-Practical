import re

s = input("Enter sentence: ")
print(re.findall(r'\b(\w+)\s+\1\b', s, re.I))