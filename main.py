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
                # elif inputed_number ==4:
                #     change_salary()
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

    empID = f"emp00{count}"

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

# def change_salary()






system()






