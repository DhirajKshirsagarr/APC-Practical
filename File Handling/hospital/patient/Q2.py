def add_patient(patient_list, patient_id, name, age):
    patient_list.append({"id": patient_id, "name": name, "age": age})

def display_patients(patient_list):
    for patient in patient_list:
        print(patient)