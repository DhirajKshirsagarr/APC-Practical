import csv
import os
import re
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

import validators as val


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "students.csv")

CSV_HEADERS = [
    "Sr No", "Submitted At",
    "Name", "Email", "Phone", "DOB", "Gender", "Address",
    "College Name", "Course", "Branch", "Year", "Semester",
]

COURSES = ["B.Tech", "B.E.", "BCA", "B.Sc", "Diploma", "M.Tech", "MCA", "M.Sc"]
BRANCHES = ["CSE", "AI & ML", "IT", "Electronics", "Mechanical", "Civil"]
YEARS = ["First", "Second", "Third", "Fourth"]
SEMESTERS = ["1", "2", "3", "4", "5", "6", "7", "8"]

MIN_AGE = 16


class RegistrationForm:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")
        self.root.geometry("900x600")
        self.root.minsize(860, 560)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.college_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.branch_var = tk.StringVar()
        self.year_var = tk.StringVar()
        self.semester_var = tk.StringVar()
        self.agree_var = tk.BooleanVar()

        self.fields = {}

        self.build_ui()

    def build_ui(self):

        tk.Label(self.root, text="Student Registration",
                 font=("Arial", 18, "bold")).pack(side="top", pady=8)

        button_row = tk.Frame(self.root)
        button_row.pack(side="bottom", pady=10)
        tk.Button(button_row, text="Submit", width=14, bg="#2e7d32", fg="white",
                  font=("Arial", 10, "bold"), command=self.submit).pack(side="left", padx=5)
        tk.Button(button_row, text="Clear", width=14,
                  command=self.clear).pack(side="left", padx=5)

        body = tk.Frame(self.root)
        body.pack(fill="both", expand=True, padx=15)

        left = tk.LabelFrame(body, text=" Personal Details ", padx=12, pady=6)
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))

        right = tk.LabelFrame(body, text=" Academic Details ", padx=12, pady=6)
        right.pack(side="left", fill="both", expand=True, padx=(8, 0))

        self.build_personal_section(left)
        self.build_academic_section(right)

    def build_personal_section(self, parent):
        self.add_entry(parent, "name", "Full Name", self.name_var, val.check_name)
        self.add_entry(parent, "email", "Email", self.email_var, val.check_email)
        self.add_entry(parent, "phone", "Phone (10 digits)", self.phone_var, val.check_phone)
        self.add_entry(parent, "dob", "Date of Birth (DD/MM/YYYY)", self.dob_var,
                       lambda v: val.check_dob(v, MIN_AGE))
        self.add_gender(parent)
        self.add_address(parent)

    def build_academic_section(self, parent):
        self.add_entry(parent, "college", "College Name", self.college_var, val.check_college)
        self.add_combo(parent, "course", "Course Name", self.course_var, COURSES, val.check_course)
        self.add_combo(parent, "branch", "Branch", self.branch_var, BRANCHES, val.check_branch)
        self.add_combo(parent, "year", "Year", self.year_var, YEARS, val.check_year,
                       also_recheck=["semester"])
        self.add_combo(parent, "semester", "Semester", self.semester_var, SEMESTERS,
                       lambda v: val.check_semester(v, self.year_var.get(), YEARS))
        self.add_agree(parent)

    def add_label(self, parent, text):
        tk.Label(parent, text=text, anchor="w").pack(fill="x", pady=(4, 0))

    def register(self, parent, key, getter, validator):
        error_label = tk.Label(parent, text="", fg="red", anchor="w", font=("Arial", 8))
        error_label.pack(fill="x")
        self.fields[key] = (getter, validator, error_label)

    def add_entry(self, parent, key, label, var, validator):
        self.add_label(parent, label)
        entry = tk.Entry(parent, textvariable=var)
        entry.pack(fill="x")
        entry.bind("<FocusOut>", lambda e: self.validate(key))
        self.register(parent, key, var.get, validator)

    def add_combo(self, parent, key, label, var, values, validator, also_recheck=()):
        self.add_label(parent, label)
        combo = ttk.Combobox(parent, textvariable=var, values=values, state="readonly")
        combo.pack(fill="x")
        combo.bind("<<ComboboxSelected>>",
                   lambda e: self.on_combo_change(key, also_recheck))
        self.register(parent, key, var.get, validator)

    def on_combo_change(self, key, also_recheck):
        self.validate(key)
        for other in also_recheck:
            getter = self.fields[other][0]
            if getter():
                self.validate(other)

    def add_gender(self, parent):
        self.add_label(parent, "Gender")
        row = tk.Frame(parent)
        row.pack(fill="x")
        for g in ("Male", "Female", "Other"):
            tk.Radiobutton(row, text=g, value=g, variable=self.gender_var,
                           command=lambda: self.validate("gender")).pack(side="left", padx=(0, 10))
        self.register(parent, "gender", self.gender_var.get, val.check_gender)

    def add_address(self, parent):
        self.add_label(parent, "Address")
        self.address_text = tk.Text(parent, height=3, width=35)
        self.address_text.pack(fill="x")
        self.address_text.bind("<FocusOut>", lambda e: self.validate("address"))
        self.register(parent, "address", self.get_address, val.check_address)

    def add_agree(self, parent):
        tk.Checkbutton(parent, text="I confirm the details are correct",
                       variable=self.agree_var,
                       command=lambda: self.validate("agree")).pack(anchor="w", pady=(10, 0))
        self.register(parent, "agree", self.agree_var.get, val.check_agree)

    def get_address(self):
        return self.address_text.get("1.0", "end-1c").strip()

    def validate(self, key):
        getter, validator, error_label = self.fields[key]
        message = validator(getter())
        error_label.config(text=message)
        return message == ""

    def validate_all(self):
        results = [self.validate(key) for key in self.fields]
        return all(results)

    def submit(self):
        if not self.validate_all():
            messagebox.showerror("Invalid form", "Please fix the errors shown in red.")
            return

        try:
            serial = self.prepare_csv()
            self.write_row(serial)
        except PermissionError:
            messagebox.showerror("File error",
                                 "Cannot write to students.csv.\n"
                                 "Close it if it is open in Excel and try again.")
            return

        messagebox.showinfo("Success",
                            f"Registration #{serial} saved!\n\nFile:\n{CSV_FILE}")
        self.clear()

    def prepare_csv(self):
        if not os.path.exists(CSV_FILE):
            return 1

        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))

        if not rows or rows[0] != CSV_HEADERS:
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            os.replace(CSV_FILE, CSV_FILE.replace(".csv", f"_old_{stamp}.csv"))
            return 1

        return len(rows)

    def write_row(self, serial):
        record = [
            serial,
            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            self.name_var.get().strip(),
            self.email_var.get().strip(),
            self.phone_var.get().strip(),
            self.dob_var.get().strip(),
            self.gender_var.get(),
            self.get_address().replace("\n", " "),
            self.college_var.get().strip(),
            self.course_var.get(),
            self.branch_var.get(),
            self.year_var.get(),
            self.semester_var.get(),
        ]

        new_file = not os.path.exists(CSV_FILE)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new_file:
                writer.writerow(CSV_HEADERS)
            writer.writerow(record)

    def clear(self):
        for var in (self.name_var, self.email_var, self.phone_var, self.dob_var,
                    self.gender_var, self.college_var, self.course_var,
                    self.branch_var, self.year_var, self.semester_var):
            var.set("")
        self.agree_var.set(False)
        self.address_text.delete("1.0", "end")
        for _, _, error_label in self.fields.values():
            error_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    RegistrationForm(root)
    root.mainloop()
