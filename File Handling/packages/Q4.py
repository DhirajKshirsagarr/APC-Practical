from texttools import cleaning, tokenization, frequency

text = "Hello, world! Hello again."
cleaned = cleaning.remove_punctuation(text)
words = tokenization.tokenize(cleaned)
freq = frequency.word_frequency(words)

print("Cleaned text:", cleaned)
print("Tokens:", words)
print("Frequency:", freq)