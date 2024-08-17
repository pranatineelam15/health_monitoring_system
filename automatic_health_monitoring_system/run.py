import os
def display_report(patient_id):
    filename = f"patient_{patient_id}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print("No existing report found for this patient.")
def create_update_report(patient_id):
    print("Enter the following diagnosis information:")
    name = input("Patient Name: ")
    age = input("Age: ")
    gender = input("Gender (M/F/O): ")
    height = input("Height (in cm): ")
    weight = input("Weight (in kg): ")
    blood_type = input("Blood Type: ")
    blood_pressure = input("Blood Pressure (e.g., 120/80 mmHg): ")
    sugar_level = input("Sugar Level (e.g., 140 mg/dL): ")
    temperature = input("Body Temperature (in °F): ")
    heart_rate = input("Heart Rate (in bpm): ")
    additional_notes = input("Additional Medical Notes (if any): ")
    diagnosis_info = (
        f"Patient ID: {patient_id}\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Gender: {gender}\n"
        f"Height: {height} cm\n"
        f"Weight: {weight} kg\n"
        f"Blood Type: {blood_type}\n"
        f"Blood Pressure: {blood_pressure} mmHg\n"
        f"Sugar Level: {sugar_level} mg/dL\n"
        f"Body Temperature: {temperature} °F\n"
        f"Heart Rate: {heart_rate} bpm\n"
        f"Additional Notes: {additional_notes}\n"
    )
    filename = f"patient_{patient_id}.txt"
    with open(filename, 'w') as file:
        file.write(diagnosis_info)
    print(f"Diagnosis report for patient {patient_id} has been saved.")
def health_monitoring_system():
    while True:
        print("\n--- Automatic Health Monitoring System ---")
        print("1. Create or Update Patient Report")
        print("2. View Existing Patient Report")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            patient_id = input("Enter patient ID: ")
            create_update_report(patient_id)
        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            display_report(patient_id)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    health_monitoring_system()