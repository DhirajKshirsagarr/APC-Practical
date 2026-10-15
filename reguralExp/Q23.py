import re

s = input("Enter Python code: ")
comments = re.findall(r'#.*', s)

print("Comments:", comments)