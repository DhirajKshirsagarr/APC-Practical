string = input("Enter a string: ")

char = input("Enter character: ")

count = 0

for ch in string:
    if ch == char:
        count += 1

print("Frequency =", count)