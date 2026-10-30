text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
most_frequent = max(frequency, key=frequency.get)
print("Most frequently occurring character:", most_frequent)
print("Frequency:", frequency[most_frequent])


