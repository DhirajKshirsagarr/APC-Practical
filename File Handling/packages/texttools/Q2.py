import string

def remove_punctuation(text):
    result = ""
    for ch in text:
        if ch not in string.punctuation:
            result = result + ch
    return result

def remove_extra_spaces(text):
    return " ".join(text.split())