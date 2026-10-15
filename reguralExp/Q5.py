import re

s = input("Enter text (use \\t or \\n for tab/newline): ")
print(re.findall(r'[ \t\n]', s))