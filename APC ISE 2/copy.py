
with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
    for line in file1:
        file2.write(line.upper())

print("file copied successfully");