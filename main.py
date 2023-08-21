def system():
    print("Welcome to our system:)")
    correct_username = "admin"
    correct_password = "admin123123"
    max_attempts = 5

    attempts = 0

    while attempts < max_attempts:
        inputed_username = input("Enter your username: ")
        inputed_password = input("Enter your password: ")

        if inputed_username == correct_username and inputed_password == correct_password:
            while True:
                print("1. to Display Statistics")
                print("2. to Add an Employee")
                print("3. to Display all Employees")
                print("4. to Change Employee's Salary")
                print("5. to Remove Employee")
                print("6. to Raise Employee's Salary")
                print("7. to exit")

                inputed_number = int(input(" "))
                if inputed_number == 1:
                    display_gender()
                elif inputed_number == 3:
                    display_users()
                elif inputed_number == 2:
                    add_employee()
                elif inputed_number ==4:
                    change_salary()
                elif inputed_number == 5:
                    remove_employee()
                elif inputed_number == 6:
                    raise_salary()
                elif inputed_number == 7:
                    exit_system()

            break





        else:
            found = False

            # Check if the inputed_username exists in data.txt
            with open('data.txt') as f:
                for line in f:
                    items = line.strip().split(', ')
                    if len(items) >= 2:  # Make sure there are at least two elements
                        username = items[1]  # Assuming the username is the second item in the line
                        if inputed_username == username:
                            found = True
                            break

            if found:
                if inputed_password == "":
                    print("Welcome user")
                    break
                else:
                    print("Invalid password")
            else:
                print("Invalid username")

        attempts += 1

    if attempts == max_attempts:
        print("Error")



#-------------------------------------------------------------------------
def display_gender():
    # https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
        male_count = 0
        female_count = 0

        with open('data.txt') as f:
            for line in f:
                line = line.strip()
                items = line.split(', ')
                gender = items[3]  # Assuming gender is the fourth item in the line
                if gender == 'male':
                    male_count += 1
                elif gender == 'female':
                    female_count += 1

            print("Male employees:", male_count)
            print("Female employees:", female_count)
            print("\n")



#-----------------------------------------------------


import datetime

def add_employee():
    file = "data.txt"

    name = input("Enter employee name: ")
    gender = input("Enter employee gender: ")

    while True:
        try:
            salary = int(input("Enter employee salary: "))
            break
        except ValueError:
            print("Invalid salary!")

    with open(file, "r") as file_read:
        count = sum(1 for _ in file_read)

    empID = f"emp00{count+1}"  # Incrementing the count by 1

    current_date = datetime.datetime.now().strftime("%Y%m%d")
    employee_data = f"{empID}, {name}, {current_date}, {gender}, {salary}"

    if gender.lower() not in ["male", "female"]:
        print("Wrong gender")
    else:
        with open(file, "a") as file_append:
            file_append.write(employee_data + "\n")
            print("Data added successfully!\n")


#----------------------------------------------------
def display_users():
    # https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
    data_dict = {}
    with open('data.txt') as f:
        for line in f:
            line = line.strip()
            items = line.split(', ')
            key = items[0]
            values = items[1:]
            data_dict[key] = values

    for key, values in data_dict.items():
        print(f"'{key}': {values}")
    print("\n")

#----------------------------------------------------

def change_salary():
    #https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file


    with open('data.txt', 'r') as file:
        filedata = file.read()


    emp_id_to_change = input("Enter the employee ID whose salary you want to change: ")
    new_salary = input("Enter the new salary: ")


    updated_lines = []

    # Iterate through each line in the file
    with open('data.txt', 'r') as file_read:
        for line in file_read:
            # Check if the line starts with the specified employee ID
            if line.startswith(emp_id_to_change): #https://www.programiz.com/python-programming/methods/string/startswith
                line = line.rsplit(', ', 1)[0] + f", {new_salary}\n"
            updated_lines.append(line)


    with open('data.txt', 'w') as file_write:
        file_write.writelines(updated_lines)


    # Check if any line starts with the specified employee ID in the updated lines
    if any(line.startswith(emp_id_to_change) for line in updated_lines):
        print(f"Salary for employee '{emp_id_to_change}' changed successfully.")
    else:
        print(f"Employee with ID '{emp_id_to_change}' not found.")

#-------------------------------------------------------------------------------


def remove_employee():
    # https://www.geeksforgeeks.org/how-to-delete-data-from-file-in-python/

    emp_remove = input("Enter the ID of the employee you want to remove: ")

    # Open the file in read mode
    with open("data.txt", "r") as f:
        # Read data line by line
        data = f.readlines()

    found = False  # Flag to track if the employee ID was found

    # Open the file in write mode
    with open("data.txt", "w") as f:
        for line in data:
            # Extract employee ID from the line
            emp_id = line.split(",")[0].strip()

            # Condition for data to be deleted based on employee ID
            if emp_id != emp_remove:
                f.write(line)
            else:
                found = True  # Employee ID was found

    if found:
        print("Employee has been removed!")
    else:
        print("Wrong employee ID")


#-------------------------------------------------------------------

def raise_salary():
    file_path = 'data.txt'
    emp_raise = input("Enter the employee ID whose salary you want to raise: ")

    while True:
        try:
            new_percentage = float(input("Enter the percentage to raise the salary by (between 0 and 100): "))
            if 0 <= new_percentage <= 100:
                break
            else:
                print("Percentage should be between 0 and 100.")
        except ValueError:
            print("Invalid percentage input.")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []

    for line in lines:
        if line.startswith(emp_raise):
            parts = line.strip().rsplit(', ', 2)
            emp_id, emp_data, salary = parts
            try:
                current_salary = int(salary)
                new_salary = current_salary * (1 + new_percentage / 100)
                updated_line = f"{emp_id}, {emp_data}, {int(new_salary)}\n"
                updated_lines.append(updated_line)
                print(f"Salary for employee '{emp_raise}' changed successfully.")
            except ValueError:
                print("Invalid salary value in data file.")
                return
        else:
            updated_lines.append(line)

    with open(file_path, 'w') as file_write:
        file_write.writelines(updated_lines)

    if not any(line.startswith(emp_raise) for line in updated_lines):
        print(f"Employee with ID '{emp_raise}' not found.")

#--------------------------------------------------------------------------------------













system()






