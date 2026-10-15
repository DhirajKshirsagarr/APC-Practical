import re

s = input("Enter post: ")
print(re.findall(r'(?<!\w)#[A-Za-z0-9_]+', s))