patients = []
next_id = 1

def add_patient():
    global next_id
    name = input("Enter patient's name: ").strip()
    age = input("Enter patient's age: ").strip()
    gender = input("Enter patient's gender(M/F/Other): ").strip()
    disease = input("Enter patient's disease/diagnosis: ").strip()
    doctor = input("Enter assigned doctor: ").strip()

    patient = {
        'id': next_id,
        'name': name,
        'age': age,
        'gender': gender,
        'disease': disease,
        'doctor': doctor,
        'status': 'Admitted'
    }
    patients.append(patient)
    next_id += 1
    print(f"Patient {name} added successfully with ID {patient['id']}.\n")

def view_patients():
    if not patients:
        print("No patients record found.\n")
        return

    print("\n{:<5} {:<15} {:<5} {:<5} {:<15} {:<15} {:<10}".format("ID", "Name", "Age", "Gender", "Disease", "Doctor", "Status"))
    print("-" * 70)
    for patient in patients:
        print("{:<5} {:<15} {:<5} {:<5} {:<15} {:<15} {:<10}".format(
            patient['id'], patient['name'], patient['age'], patient['gender'],
            patient['disease'], patient['doctor'], patient['status']))
    print()

def find_by_id(patient_id):
    for patient in patients:
        if patient['id'] == patient_id:
            return patient
    return None

def search_patients():
    if not patients:
        print("No patients record found.\n")
        return

    keyword = input("Enter patient's ID or name to search: ").strip()
    results = []

    for patient in patients:
        if keyword.isdigit() and patient['id'] == int(keyword):
            results.append(patient)
        elif keyword.lower() in patient['name'].lower():
            results.append(patient)

    if not results:
        print("No matching patients found.\n")
        return

    for patient in results:
        print(f"\nPatient ID: {patient['id']}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Gender: {patient['gender']}")
        print(f"Disease/Diagnosis: {patient['disease']}")
        print(f" Doctor: {patient['doctor']}")
        print(f"Status: {patient['status']}")
    print()

def update_patient():
    if not patients:
        print("No patients record found.\n")
        return

    patient_id = input("Enter patient's ID to update: ").strip()
    if not patient_id.isdigit():
        print("Invalid ID.\n")
        return

    patient = find_by_id(int(patient_id))
    if not patient:
        print("Patient not found.\n")
        return

    print("Leave field blank to keep current value.")
    name = input(f"Enter new name (current: {patient['name']}): ").strip()
    age = input(f"Enter new age (current: {patient['age']}): ").strip()
    gender = input(f"Enter new gender (current: {patient['gender']}): ").strip()
    disease = input(f"Enter new disease/diagnosis (current: {patient['disease']}): ").strip()
    doctor = input(f"Enter new doctor (current: {patient['doctor']}): ").strip()

    if name:
        patient['name'] = name
    if age:
        patient['age'] = age
    if gender:
        patient['gender'] = gender
    if disease:
        patient['disease'] = disease
    if doctor:
        patient['doctor'] = doctor

    print(f"Patient {patient['name']} updated successfully.\n")

def discharge_patient():
    if not patients:
        print("No patients record found.\n")
        return

    patient_id = input("Enter patient's ID to discharge: ").strip()
    if not patient_id.isdigit():
        print("Invalid ID.\n")
        return

    patient = find_by_id(int(patient_id))
    if not patient:
        print("Patient not found.\n")
        return

    if patient['status'] == 'Discharged':
        print(f"Patient {patient['name']} is already discharged.\n")
        return

    patient['status'] = 'Discharged'
    print(f"Patient {patient['name']} has been discharged successfully.\n")

def delete_patient():
    if not patients:
        print("No patients record found.\n")
        return

    patient_id = input("Enter patient's ID to delete: ").strip()
    if not patient_id.isdigit():
        print("Invalid ID.\n")
        return

    patient = find_by_id(int(patient_id))
    if not patient:
        print("Patient not found.\n")
        return

    patients.remove(patient)
    print(f"Patient {patient['name']} has been deleted successfully.\n")

def menu():
    while True:
        print("Hospital Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Discharge Patient")
        print("6. Delete Patient")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patients()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            discharge_patient()
        elif choice == '6':
            delete_patient()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()