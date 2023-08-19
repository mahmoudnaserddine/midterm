def view_data():
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


#------------------------------------------------------------

def system():
    print("Welcome to our sytem:)")
    correct_username = "admin"
    correct_password = "admin123123"
    max_attempts = 5

    attempts = 0

    while attempts < max_attempts:
        inputed_username = input("Enter your username: ")
        inputed_password = input("Enter your password: ")

        if inputed_username == correct_username and inputed_password == correct_password:
            while True:
                print("press 1 to Display Statistics")
                print("press 2 to Add an Employee")
                print("press 3 to Display all Employees")
                print("press 4 to Change Employee's Salary")
                print("press 5 to Remove Employee")
                print("press 6 to Raise Employee's Salary")
                print("press 7 to exit")

                inputed_number = int(input(" "))
                if inputed_number == 1:
                    display_gender()
                elif inputed_number == 3:
                    display_users()
            break





        else:
            found = False

            # Check if the inputed_username exists in data.txt
            with open('data.txt') as f:
                for line in f:
                    username = line.split(', ')[1]  # Assuming the username is the second item in the line
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



#----------------------------------------------------
def display_users():
        view_data()




system()






