def is_eligible(attended, total):
    percent = (attended / total) * 100
    return percent >= 75