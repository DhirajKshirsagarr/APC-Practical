def add_record(record_list, patient_id, diagnosis):
    record_list.append({"patient_id": patient_id, "diagnosis": diagnosis})

def display_records(record_list):
    for record in record_list:
        print(record)