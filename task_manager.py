from datetime import datetime, date

# Function to register a new user
def reg_user(u_username):
    if u_username == "admin":
        Userlist = []
        Condition = True
        u_username_reg = input("Please enter a new username: ").lower()

        with open('user.txt', 'r') as usertext:
            for line in usertext:
                listusr = line.split(', ')
                if listusr[0] == u_username_reg:
                    print(f"User {u_username_reg} already exists!")
                    Condition = False
        if u_username_reg == "" or u_username_reg == " ":
            print("Error, invalid username!")
            Condition = False
        usertext.close()

        if Condition:
            u_password_reg = input("Please enter a new password: ")
            u_passwordconfirm_reg = input("Please confirm your password: ")

            if u_password_reg == u_passwordconfirm_reg:
                with open('user.txt', 'a+') as usertext:
                    Userlist.append(u_username_reg)
                    Userlist.append(u_password_reg)
                    PrintToTxt = ", ".join(Userlist)
                    usertext.write("\n" + PrintToTxt)
                print(f"Success! User {u_username_reg} is now registered!")
            else:
                print("Passwords do not match.")
    else:
        print("\nYou need to be an admin to register new users!")

# Function to add a task
# Function to add a task
# Function to add a task
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to add a task
def add_task(u_username_task, u_title_task, u_desc_task, u_duedate_task_y, u_duedate_task_m, u_duedate_task_d, date_assigned, task_completed):
    # Initialize Tasklist as an empty list
    Tasklist = []

    with open('tasks.txt', 'r') as tasktext:
        for line in tasktext:
            # Strip whitespace characters, including the newline character
            line = line.strip()
            if line:  # Check if line is not empty
                Tasklist = line.split(', ')
    
    if Tasklist:
        task_counter = int(Tasklist[-1])  # Update the task_counter from the last task in the file
    else:
        task_counter = 0

    task_counter += 1  # Increment task_counter for the new task

    while True:
        u_duedate_task = f"{u_duedate_task_y}-{u_duedate_task_m:02d}-{u_duedate_task_d:02d}"
        if is_valid_date(u_duedate_task):
            break
        else:
            print("Invalid date format. Please enter the date in the format (YYYY-MM-DD).")
            u_duedate_task_y = int(input("Please enter the due date for the task (year): "))
            u_duedate_task_m = int(input("Please enter the due date for the task (month): "))
            u_duedate_task_d = int(input("Please enter the due date for the task (day): "))

    with open('tasks.txt', 'a+') as tasktext:
        Tasklist.append(u_username_task)
        Tasklist.append(u_title_task)
        Tasklist.append(u_desc_task)
        Tasklist.append(u_duedate_task)
        Tasklist.append(date_assigned)
        Tasklist.append(task_completed)
        Tasklist.append(str(task_counter))
        PrintToTxt = ", ".join(Tasklist)
        tasktext.write("\n" + PrintToTxt)

    print("Success!")


# Function to view all tasks
def view_all():
    print("All Tasks:")
    with open('tasks.txt', 'r') as tasktext:
        for index, line in enumerate(tasktext, start=1):
            Tasklist = line.strip().split(', ')
            if len(Tasklist) >= 7:  # Ensure Tasklist contains at least 7 elements
                print(f'''
                _________________________________________

                Task Nr: {index}
                Name: {Tasklist[0]}
                Task: {Tasklist[1]}
                Description: {Tasklist[2]}
                Due Date: {Tasklist[3]}
                Date Assigned: {Tasklist[4]}
                Completion Status: {Tasklist[5]}
                _________________________________________
                ''')
            else:
                print("Invalid task format. Skipping...")

# Function to view tasks for the logged-in user
# Function to view tasks for the logged-in user
def view_mine(u_username):
    with open('tasks.txt', 'r') as tasktext:
        for index, line in enumerate(tasktext, start=1):
            Tasklist = line.strip().split(', ')
            if u_username == Tasklist[0]:
                print(f'''
                _________________________________________

                Task Nr: {index}
                Name: {Tasklist[0]}
                Task: {Tasklist[1]}
                Description: {Tasklist[2]}
                Due Date: {Tasklist[3]}
                Date Assigned: {Tasklist[4]}
                Completion Status: {Tasklist[5]}
                _________________________________________
                ''')


# Function to view and update tasks for the logged-in user
def view_my_tasks(u_username):
    task_list = []
    user_task_counter = {}  # New dictionary to store a task counter for each user

    # Read all tasks and store them in task_list
    with open('tasks.txt', 'r') as tasktext:
        for line in tasktext:
            Tasklist = line.strip().split(', ')
            task_list.append(Tasklist)
            username = Tasklist[0]
            if username not in user_task_counter:
                user_task_counter[username] = 0

    print(f"Tasks for user {u_username}:")
    for task in task_list:
        if u_username == task[0]:
            user_task_counter[u_username] += 1
            task_number = user_task_counter[u_username]  # Calculate task number for the current user
            print(f'''
                _________________________________________

                Task Nr: {task_number}
                Name: {task[0]}
                Task: {task[1]}
                Description: {task[2]}
                Due Date: {task[3]}
                Date Assigned: {task[4]}
                Completion Status: {task[5]}
                _________________________________________
                ''')

    selection = input("Please select a task using the task nr or '-1' to return to the main menu: ")
    if selection == '-1':
        return

    selection = int(selection)
    for task in task_list:
        if int(task[6]) == selection and task[0] == u_username:
            selection2 = int(input("Press 1 for 'Mark as complete' or 2 for 'Edit task': "))
            if selection2 == 1:
                task[5] = "Yes"
                print("Task marked as complete.")
            elif selection2 == 2:
                if task[5] == "No":
                    duedate_task_y = int(input("Please enter the new due date for the task (year): "))
                    duedate_task_m = int(input("Please enter the new due date for the task (month): "))
                    duedate_task_d = int(input("Please enter the new due date for the task (day): "))
                    task[3] = f"{duedate_task_y}-{duedate_task_m}-{duedate_task_d}"
                    print("Task edited successfully.")
                else:
                    print("Only uncompleted tasks can be edited.")

    # Write all the tasks back to the file
    with open('tasks.txt', 'w') as tasktext:
        for task in task_list:
            PrintToTxt = ", ".join(task)
            tasktext.write(PrintToTxt + "\n")

    print("Task list updated successfully.")






# Function to display statistics
def stat(u_username):
    task_counter = 0
    user_counter = 0
    if u_username == "admin":
        print("\n_________________________________________\n\nGood day admin, the stats are as follows: \n_________________________________________\n")
        with open('tasks.txt', 'r') as tasktext:
            for line in tasktext:
                task_counter += 1
        with open('user.txt', 'r') as usertext:
            for line in usertext:
                user_counter += 1
        print(f"Total amount of users: {user_counter}")
        print(f"Total amount of tasks: {task_counter}\n_________________________________________\n")
    else:
        print("You're not an admin!")

    # Display the content of the task_overview.txt and user_overview.txt files
    if u_username == "admin":
        try:
            with open('task_overview.txt', 'r') as taskoverviewtxt:
                print("Task Overview:")
                for line in taskoverviewtxt:
                    print(line.strip())
            print("\n")
        except FileNotFoundError:
            print("Task Overview file not found.")
            
    try:
        with open('user_overview.txt', 'r') as useroverviewtxt:
            print("User Overview:")
            for line in useroverviewtxt:
                print(line.strip())
    except FileNotFoundError:
        print("User Overview file not found.")

def reports(u_username):
    comp_counter = 0
    incomp_counter = 0
    incomp_overdue = 0
    task_counter = 0

    with open('tasks.txt', 'r') as tasktext:
        for line in tasktext:
            task_counter += 1
            Tasklist = line.split(', ')
            if Tasklist[5] == "No":
                incomp_counter += 1
                if datetime.strptime(Tasklist[3], "%Y-%m-%d").date() < date.today():
                    incomp_overdue += 1
            elif Tasklist[5] == "Yes":
                comp_counter += 1

    percent_incomplete = (incomp_counter / task_counter) * 100
    percent_overdue = (incomp_overdue / task_counter) * 100

    with open('task_overview.txt', "w+") as taskoverviewtxt:
        taskoverviewtxt.writelines(f"Tasks completed: {comp_counter}\n")
        taskoverviewtxt.writelines(f"Tasks not completed: {incomp_counter}\n")
        taskoverviewtxt.writelines(f"Tasks overdue: {incomp_overdue}\n")
        taskoverviewtxt.writelines(f"Task % incompleted: {percent_incomplete:.2f}\n")
        taskoverviewtxt.writelines(f"Task % overdue: {percent_overdue:.2f}\n")

    if u_username == "admin":
        with open('user_overview.txt', "w+") as useroverviewtxt:
            with open('user.txt', 'r') as usertext:
                for line in usertext:
                    user = line.split(', ')[0]
                    user_task_counter = 0
                    user_comp_counter = 0
                    user_incomp_counter = 0
                    user_incomp_overdue = 0
                    with open('tasks.txt', 'r') as tasktext:
                        for line in tasktext:
                            Tasklist = line.split(', ')
                            if user == Tasklist[0]:
                                user_task_counter += 1
                                if Tasklist[5] == "No":
                                    user_incomp_counter += 1
                                    if datetime.strptime(Tasklist[3], "%Y-%m-%d").date() < date.today():
                                        user_incomp_overdue += 1
                                elif Tasklist[5] == "Yes":
                                    user_comp_counter += 1

                    if user_task_counter == 0:
                        user_percent_incomplete = 0
                        user_percent_overdue = 0
                    else:
                        user_percent_incomplete = (user_incomp_counter / user_task_counter) * 100
                        user_percent_overdue = (user_incomp_overdue / user_task_counter) * 100

                    useroverviewtxt.writelines(f'''
                    _________________________________________
                    User: {user}                      
                    Tasks completed: {user_comp_counter}
                    Tasks not completed: {user_incomp_counter}
                    Tasks overdue: {user_incomp_overdue}
                    Task % incompleted: {user_percent_incomplete:.2f}  
                    Task % overdue: {user_percent_overdue:.2f}  
                    _________________________________________
                    \n''')

    print("Reports generated successfully.")


# Login Section
listpassw = []
listusr = []
loginstatus = "false"
task_counter = 0  # Initialize the task counter

while loginstatus == "false":
    u_username = input("Please enter your username: ").lower()

    with open('user.txt', 'r') as usertext:
        for line in usertext:
            listusr = line.split(', ')
            if listusr[0] == u_username:
                u_password = input(f"Please enter your password {u_username}: ")
                if listusr[1] == "\n" + u_password or listusr[1] == u_password + "\n" or listusr[1] == u_password:
                    loginstatus = "True"
                    print(f"\nSuccess! Welcome {u_username}.")
                    break
                else:
                    print(f"Incorrect password for {u_username}.")
        if u_username == "" or u_username == " ":
            print("Error, invalid username!")
    usertext.close()

while True:
    if u_username == "admin":
        menu = input('''\nSelect one of the following options below:\n
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - view stats
gr - generate reports
e - Exit
    
\nPlease enter your selection: ''').lower()

    else:
        menu = input('''\nSelect one of the following options below:\n
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
    
\nPlease enter your selection: ''').lower()
                
    if menu == 'r':
        reg_user(u_username)

    elif menu == 'a':
        Tasklist = []
        u_username_task = input("Please enter the username for the task: ").lower()
        u_title_task = input("Please enter the title of the task: ").lower()
        u_desc_task = input("Please enter the description of the task: ").lower()
        u_duedate_task_y = int(input("Please enter the due date for the task (year): "))
        u_duedate_task_m = int(input("Please enter the due date for the task (month): "))
        u_duedate_task_d = int(input("Please enter the due date for the task (day): "))
        date_assigned = str(date.today())
        task_completed = "No"

        add_task(u_username_task, u_title_task, u_desc_task, u_duedate_task_y, u_duedate_task_m, u_duedate_task_d, date_assigned, task_completed)

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_my_tasks(u_username)

    elif menu == 's':
        stat(u_username)
    elif menu == 'e':
        print('Goodbye!')
        exit()
    elif menu == 'gr':
        reports(u_username)
            
    else:
        print("You have made a wrong choice, Please Try again")
