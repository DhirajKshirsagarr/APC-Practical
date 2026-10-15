import re

s = input("Enter research paper references: ")

print("DOIs:", re.findall(r'\b10\.\d{4,9}/[^\s]+', s))
print("Years:", re.findall(r'\b(?:19|20)\d{2}\b', s))
print("Emails:", re.findall(r'[\w.-]+@[\w.-]+\.\w+', s))
print("URLs:", re.findall(r'https?://\S+', s))