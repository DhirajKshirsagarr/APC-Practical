import re

s = input("Enter a sentence: ")
print("Word count:", len(re.findall(r'\b\w+\b', s)))