def total_marks(marks_list):
    return sum(marks_list)

def percentage(marks_list, max_marks):
    return (sum(marks_list) / max_marks) * 100

def grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    else:
        return "D"