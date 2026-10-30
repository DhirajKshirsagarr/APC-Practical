from patient import management as patient_mgmt
from doctor import management as doctor_mgmt
from billing import billing
from records import medical_records

patient_list = []
doctor_list = []
record_list = []

patient_mgmt.add_patient(patient_list, "P1", "Rehan", 21)
doctor_mgmt.add_doctor(doctor_list, "D1", "Dr. Sharma", "Cardiology")
medical_records.add_record(record_list, "P1", "Routine Checkup")

patient_mgmt.display_patients(patient_list)
doctor_mgmt.display_doctors(doctor_list)
medical_records.display_records(record_list)

billing.generate_bill("Rehan", 1500)    