
# 1. Class Exercise:
# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule.


class HospitalAccount:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.schedule = {}

    def schedule_visit(self, patient_name, date):
        if patient_name not in self.schedule:
            self.schedule[patient_name] = [date]
        else:
            self.schedule[patient_name].append(date)
        return f"Visit scheduled for {patient_name} on {date}"

    def remove_schedule(self, patient_name, date):
        if patient_name in self.schedule and date in self.schedule[patient_name]:
            self.schedule[patient_name].remove(date)
            return f"Visit removed for {patient_name} on {date}"
        else:
            return f"No visit found for {patient_name} on {date}"


hospital = HospitalAccount("Holy Mary")
print(hospital.schedule_visit("George Sawyer", "12/3/2024"))
print(hospital.remove_schedule("George Sawyer", "12/3/2024"))
print(hospital.remove_schedule("Tim Smith", "2/10/2024"))
print(hospital.remove_schedule("George Sawyer", "12/3/2024"))
