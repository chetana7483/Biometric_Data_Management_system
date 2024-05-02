class BiometricData:
    def __init__(self, name, age, DoB, nationality, id_number, biometric_type, visa_number):
        self.name = name
        self.age = age
        self.DoB = DoB
        self.nationality = nationality
        self.id_number = id_number
        self.biometric_type = biometric_type
        self.visa_number = visa_number

class BiometricDataManager:
    def __init__(self, file_path):
        self.data = {}
        self.enroll_data = []
        self.file_path = file_path
        self.load_data_from_file()

    def load_data_from_file(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    id_number = data[4]  # Assuming id_number is in the fifth position
                    name = data[0]
                    age = int(data[1])
                    DoB = data[2]
                    nationality = data[3]
                    biometric_type = data[5]
                    visa_number = data[6]
                    self.data[id_number] = BiometricData(name, age, DoB, nationality, id_number, biometric_type, visa_number)
        except FileNotFoundError:
            print("Data file not found. Starting with an empty database.")

    def save_data_to_file(self):
        with open(self.file_path, 'w') as file:
            for data in self.data.values():
                file.write(f"{data.name},{data.age},{data.DoB},{data.nationality},{data.id_number},{data.biometric_type},{data.visa_number}\n")

    def create_Data(self, Data):
        if Data.id_number not in self.data:
            self.data[Data.id_number] = Data
            self.save_data_to_file()  # Save to file after adding new data
            print(f"Biometric data added for {Data.name}")
        else:
            print(f"id number {Data.id_number} already exists in the database.")

    def delete_Data(self, id_number):
        if id_number in self.data:
            del self.data[id_number]
            self.save_data_to_file()  # Save to file after deleting data
            print("Biometric data deleted successfully.")
        else:
            print("id number not found in the database.")

    def update_Data(self, id_number):
        if id_number in self.data:
            old_data = self.data[id_number]
            name = input("Enter new name (leave it blank to keep it as it is): ")
            age = input("Enter new age: ")
            DoB = input("Enter new DoB(DD-MM-YY): ")
            nationality = input("Enter new nationality: ")
            biometric_type = input("Enter new biometric_type: ")
            visa_number = input("Enter new visa number: ")

            if name == "":
                name = old_data.name

            if age == "":
                age = old_data.age
            else:
                age = int(age)

            if DoB == "":
                DoB = old_data.DoB

            if nationality == "":
                nationality = old_data.nationality

            if biometric_type == "":
                biometric_type = old_data.biometric_type

            if visa_number == "":
                visa_number = old_data.visa_number

            new_Data = BiometricData(name, age, DoB, nationality, id_number, biometric_type, visa_number)
            self.data[id_number] = new_Data
            self.save_data_to_file()  # Save to file after updating data
            print("Biometric data updated successfully.")
        else:
            print("id number not found in the database.")

    def verify_Data(self, id_number):
        if id_number in self.data:
            print("Biometric Data verified successfully.")
        else:
            print("Biometric Data not found in the database.")

    def display_all(self):
        if self.data:
            for id_number, Data in self.data.items():
                print(f"ID Number: {Data.id_number}")
                print(f"Name: {Data.name}")
                print(f"Age: {Data.age}")
                print(f"DoB: {Data.DoB}")
                print(f"biometric_type: {Data.biometric_type}")
                print(f"nationality: {Data.nationality}")
                print(f"Visa Number: {Data.visa_number}")
                print()
        else:
            print("There is no Data to be displayed")

    def manage_enroll_data(self, enroll_data):
        self.enroll_data.append(enroll_data)
        print(f"Enroll data added for {enroll_data.name}")


def main():
    file_path = "biometric_data.txt"  # Specify the path to your data file
    manager = BiometricDataManager(file_path)

    while True:
        print("\n\n**************************************************")
        print("\n~~~~~~~~Menu:~~~~~~~~~")
        print("1. Create biometric data")
        print("2. Delete biometric data")
        print("3. Update biometric data")
        print("4. Verify biometric data")
        print("5. Display All")
        print("6. Manage Enroll Data")
        print("7. Exit")

        choice = input("Enter your choice: ")
        print("*****************************************************")

        if choice == '1':
            id_number = input("Enter ID number: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            DoB = input("Enter DoB(DD-MM-YY): ")
            nationality = input("Enter nationality: ")
            biometric_type = input("Enter biometric_type: ")
            visa_number = input("Enter visa number: ")
            Data = BiometricData(name, age, DoB, nationality, id_number, biometric_type, visa_number)
            manager.create_Data(Data)

        elif choice == '2':
            id_number = input("Enter id number to delete: ")
            manager.delete_Data(id_number)

        elif choice == '3':
            id_number = input("Enter ID number you want to update: ")
            manager.update_Data(id_number)

        elif choice == '4':
            id_number = input("Enter id number to verify: ")
            manager.verify_Data(id_number)

        elif choice == '5':
            manager.display_all()

        elif choice == '6':
            id_number=int(input("Enter id :"))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            DoB = input("Enter DoB(DD-MM-YY): ")
            nationality = input("Enter nationality: ")
            biometric_type = input("Enter biometric_type: ")
            visa_number = input("Enter visa number: ")
            enroll_data = BiometricData(name, age, DoB, nationality,id_number, biometric_type, visa_number)
            manager.manage_enroll_data(enroll_data)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
