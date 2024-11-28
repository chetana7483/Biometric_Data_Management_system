Biometric Data Management System
This Python project manages biometric data for individuals, including details like ID, name, age, date of birth, nationality, biometric type, and visa number. It offers file handling capabilities to persist data across sessions.

Features
Create Biometric Data: Add a new record to the database.
Delete Biometric Data: Remove a record by its ID.
Update Biometric Data: Modify details of an existing record.
Verify Biometric Data: Check if a record exists for a given ID.
Display All Data: View all stored records.
Manage Enroll Data: Add enrollment records separately.
File Handling (Optional): Save and load data from a file.
How It Works
With File Handling
Persistence: Data is stored in a text file (biometric_data.txt) and reloaded each time the program runs.
File Operations:
Save to File: After adding, updating, or deleting records, the data is written back to the file.
Load from File: Reads the file and loads the data into memory during initialization.
Advantages: Data remains available across multiple runs of the program.
Without File Handling
Temporary Data: Data is stored in memory (Python dictionaries) only during the program's execution.
Advantages: Simpler code with no file dependencies.
Disadvantages: All data is lost when the program exits.
Setup Instructions
1. With File Handling
Ensure the file biometric_data.txt exists in the same directory as the script (it will be created automatically if missing).
Run the program, and data will be saved/loaded from this file.
2. Without File Handling
Comment out or remove the load_data_from_file() and save_data_to_file() methods in the BiometricDataManager class.
Modify the create_Data, delete_Data, update_Data, and manage_enroll_data methods to skip saving data to the file.
Usage
Run the program.
Choose an option from the menu:
1 to create biometric data.
2 to delete biometric data.
3 to update biometric data.
4 to verify biometric data.
5 to display all records.
6 to manage enroll data.
7 to exit the program.
Code Adjustments for File Handling
Enable File Handling
The program is already set up for file handling. It uses:
load_data_from_file() to load data on startup.
save_data_to_file() to save data after modifications.
Disable File Handling
Remove or comment out the following calls:
self.load_data_from_file()  # In the constructor
self.save_data_to_file()    # In create_Data, delete_Data, update_Data
Example Scenarios
1. With File Handling
Add a record for an individual.
Exit and re-run the program.
View the record you added earlier (data persists).
2. Without File Handling
Add a record for an individual.
Exit and re-run the program.
The record will no longer be available.
