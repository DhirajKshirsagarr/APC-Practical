def add_doctor(doctor_list, doctor_id, name, specialization):
    doctor_list.append({"id": doctor_id, "name": name, "specialization": specialization})

def display_doctors(doctor_list):
    for doctor in doctor_list:
        print(doctor)