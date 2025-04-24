class Person:
    def __init__(self, name, nic, age):
        self.name = name
        self.nic = nic
        self.age = age


class Patient(Person):
    def __init__(self, name, nic, age, disease, days_admitted, daily_charge):
        super().__init__(name, nic, age)
        self.disease = disease
        self.days_admitted = days_admitted
        self.daily_charge = daily_charge

    def total_bill(self):
        return self.days_admitted * self.daily_charge


class Staff(Person):
    def __init__(self, name, nic, age, basic_salary):
        super().__init__(name, nic, age)
        self.basic_salary = basic_salary

    def get_salary(self):
        raise NotImplementedError("Subclasses must implement this method")


class Doctor(Staff):
    CONSULTATION_FEE = 5000

    def __init__(self, name, nic, age, basic_salary, patients_handled):
        super().__init__(name, nic, age, basic_salary)
        self.patients_handled = patients_handled

    def get_salary(self):
        return self.basic_salary + (self.CONSULTATION_FEE * self.patients_handled)


class Nurse(Staff):
    OVERTIME_RATE = 200

    def __init__(self, name, nic, age, basic_salary, overtime_hours):
        super().__init__(name, nic, age, basic_salary)
        self.overtime_hours = overtime_hours

    def get_salary(self):
        return self.basic_salary + (self.overtime_hours * self.OVERTIME_RATE)



def handle_patient():
    print("\nEnter Patient Details:")
    name = input("Name: ")
    nic = input("NIC: ")
    age = int(input("Age: "))
    disease = input("Disease: ")
    days = int(input("Days Admitted: "))
    daily_charge = float(input("Daily Charge: "))

    patient = Patient(name, nic, age, disease, days, daily_charge)
    print(f"\nTotal Bill for {patient.name}: Rs. {patient.total_bill():.2f}")


def handle_staff():
    print("\nStaff Type (1. Doctor / 2. Nurse):")
    staff_type = input("Enter choice: ").strip()
    name = input("Name: ")
    nic = input("NIC: ")
    age = int(input("Age: "))
    salary = float(input("Basic Salary: "))

    if staff_type == "1":
        patients = int(input("Number of Patients Handled: "))
        staff = Doctor(name, nic, age, salary, patients)
    elif staff_type == "2":
        overtime = int(input("Overtime Hours: "))
        staff = Nurse(name, nic, age, salary, overtime)
    else:
        print("Invalid staff type!")
        return

    print(f"\nSalary for {staff.name}: Rs. {staff.get_salary():.2f}")


def main():
    while True:
        print("\n===== Hospital Management Menu =====")
        print("1. Patient Billing")
        print("2. Staff Salary")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            handle_patient()
        elif choice == "2":
            handle_staff()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
