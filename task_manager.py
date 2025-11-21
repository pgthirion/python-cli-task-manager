#=====importing libraries===========
from datetime import datetime, date
#====Login Section====

# Asking the user for their username
# if it is equal to blank or only a space error
# otherwise proceed
# if the line = the username entered check password
# if password is correct proceed
# else error

listpassw = []
listusr = []
loginstatus = "false"

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

                else:
                    print(f"Incorrect password for {u_username}.")
        if u_username == "" or u_username == " ":
            print("Error, invalid username!")
    usertext.close()
while True:
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if u_username == "admin":
        menu = input('''\nSelect one of the following options below:\n
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - view stats
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
        if u_username == "admin": # Check if admin
            # Creating variables and gathering inputs
            Userlist =[]
            u_username_reg = input("Please enter a new username: ").lower()
            u_password_reg = input("Please enter a new password: ")
            u_passwordconfirm_reg = input("Please confirm your password: ")
            # if passwords match, register the new user
            if u_password_reg == u_passwordconfirm_reg:
                with open('user.txt', 'a+') as usertext:
                    Userlist.append(u_username_reg)
                    Userlist.append(u_password_reg)
                    PrintToTxt = ", ".join(Userlist)
                    usertext.write("\n" + PrintToTxt)
            print(f"Success! User {u_username_reg} is now registered!")
        # if not admin, error
        else:
            print("\nYou need to be an admin to register new users!")

    elif menu == 'a':
        # Creating variables and gathering inputs and converting them
        Tasklist =[]
        u_username_task = input("Please enter the username for the task: ").lower()
        u_title_task = input("Please enter the title of the task: ").lower()
        u_desc_task = input("Please enter the description of the task: ").lower()
        u_duedate_task_y = int(input("Please enter the due date for the task (year): "))
        u_duedate_task_m = int(input("Please enter the due date for the task (month): "))
        u_duedate_task_d = int(input("Please enter the due date for the task (day): "))
        date_assigned = str(date.today())
        task_completed = "No"
        # Open file
        # Write all gathered data to list
        # Print list joined into text file
        # Close file
        with open('tasks.txt', 'a+') as tasktext:
            Tasklist.append(u_username_task)        
            Tasklist.append(u_title_task)
            Tasklist.append(u_desc_task)
            Tasklist.append(f"{u_duedate_task_y}-{u_duedate_task_m}-{u_duedate_task_d}")
            Tasklist.append(date_assigned)
            Tasklist.append(task_completed)
            PrintToTxt = ", ".join(Tasklist)
            tasktext.write("\n" + PrintToTxt)
            tasktext.close()

    elif menu == 'va':
        # Create list
        Tasklist = []
        # Open file
        # Print all elements of the splitted list in the right places
        # Close file
        with open('tasks.txt', 'r') as tasktext:  
            for line in tasktext:
                Tasklist = line.split(', ')
                print(f'''
                _________________________________________
                
                Name: {Tasklist[0]}
                Task: {Tasklist[1]}
                Description: {Tasklist[2]}
                Due Date: {Tasklist[3]}
                Date Assigned: {Tasklist[4]}
                Completion Status: {Tasklist[5]}
                _________________________________________
                ''')
        tasktext.close()

    elif menu == 'vm':
        # Create list
        Tasklist = []
        # Open file
        # Loop through file and split the lines
        # print everything for the logged in user
        # Close file
        with open('tasks.txt', 'r') as tasktext:
            for line in tasktext:
                Tasklist = line.split(', ')
                if u_username == Tasklist[0]:
                    print(f'''
                    _________________________________________

                    Name: {Tasklist[0]}
                    Task: {Tasklist[1]}
                    Description: {Tasklist[2]}
                    Due Date: {Tasklist[3]}
                    Date Assigned: {Tasklist[4]}
                    Completion Status: {Tasklist[5]}
                    _________________________________________
                    ''')
        tasktext.close()

    elif menu == 's':
        task_counter = 0
        user_counter = 0
        if u_username == "admin":
            print("\n_________________________________________\n\nGood day admin, the stats are as follows: \n_________________________________________\n")
            with open('tasks.txt', 'r') as tasktext:
                for line in tasktext:
                    task_counter += +1
            with open('user.txt', 'r') as usertext:
                for line in usertext:
                    user_counter += +1
            print(f"Total amount of users: {user_counter}")
            print(f"Total amount of tasks: {task_counter}\n_________________________________________\n")
        else:
            print("You're not an admin!")
    elif menu == 'e':
        print('Goodbye!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")