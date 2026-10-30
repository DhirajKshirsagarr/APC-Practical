import re
from datetime import datetime


def check_name(value):
    value = value.strip()
    if not value:
        return "Name is required"
    if not re.fullmatch(r"[A-Za-z ]{3,50}", value):
        return "Use only letters and spaces (3-50 characters)"
    return ""


def check_email(value):
    value = value.strip()
    if not value:
        return "Email is required"
    if not re.fullmatch(r"[\w.+-]+@[\w-]+\.[\w.-]+", value):
        return "Enter a valid email, e.g. name@example.com"
    return ""


def check_phone(value):
    value = value.strip()
    if not value:
        return "Phone number is required"
    if not re.fullmatch(r"[6-9]\d{9}", value):
        return "Must be 10 digits and start with 6, 7, 8 or 9"
    return ""


def check_dob(value, min_age=16):
    value = value.strip()
    if not value:
        return "Date of birth is required"
    try:
        dob = datetime.strptime(value, "%d/%m/%Y")
    except ValueError:
        return "Use format DD/MM/YYYY (a real date)"

    today = datetime.today()
    if dob > today:
        return "Date cannot be in the future"

    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age < min_age:
        return f"Student must be at least {min_age} years old"
    return ""


def check_gender(value):
    return "" if value else "Please select a gender"


def check_address(value):
    value = value.strip()
    if not value:
        return "Address is required"
    if len(value) < 10:
        return "Address is too short (min 10 characters)"
    return ""


def check_college(value):
    value = value.strip()
    if not value:
        return "College name is required"
    if not re.fullmatch(r"[A-Za-z0-9 .,&()'-]{3,100}", value):
        return "Use letters, numbers and . , & ( ) - only (3-100 characters)"
    return ""


def check_course(value):
    return "" if value else "Please select a course"


def check_branch(value):
    return "" if value else "Please select a branch"


def check_year(value):
    return "" if value else "Please select a year"


def check_semester(value, year, years):
    if not value:
        return "Please select a semester"

    if year in years:
        position = years.index(year)
        first, second = str(2 * position + 1), str(2 * position + 2)
        if value not in (first, second):
            return f"{year} year has semesters {first} and {second}"
    return ""


def check_agree(value):
    return "" if value else "Please tick the confirmation box"

