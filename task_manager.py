# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
import sys
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

line = "-" * 35  #Border line for a better look to the output view

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]
# print(task_data)

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "yes" else False
    curr_t['task_number'] = task_components[6]
    

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
#     allow a user to login.
# '''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#Functions created for task
def reg_user():
        # Read in user_data for comparison
        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")
        # Convert to a dictionary
        username_password = {}
        for user in user_data:
            username, password = user.split(';')
            username_password[username] = password
        # # Request input of a new username
        new_username = input("New Username: ")
        #Error message if user exists in the txt file
        while new_username in username_password.keys():
            print("User already exists, Please enter a different username")
            new_username = input("New Username: ")
        # Request input of a new password and then asks for confirmation
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))
        else:
                print("Passwords do not match, please try again.")
        
            
def add_task(task_complete= "no"):
    task_username = input("Name of person assigned to task: ")
    while task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        task_username = input("Name of person assigned to task: ")
    
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()

    count = input("Task number : ")
    
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": task_complete,
        "task_number": count
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "yes" if t['completed'] else "no",
                t['task_number']
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():
    for t in task_list:
        print(line)
        disp_str = f"Task {t['task_number']}: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Complete?: \t {t['completed']}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
  
    for t in task_list:
        if t['username'] == curr_user:
            print(line)
            disp_str = f": Task {t['task_number']}\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Complete?: \t {t['completed']}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

    print("To modify completion status on a task, enter the task number otherwise enter -1 to return to main menu.")
    user_task_selection = input("Please enter the task number to complete : ")
    if user_task_selection == t['task_number']:
        t['completed'] = "yes"
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "yes" if t['completed'] else "No",
                    t['task_number']
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully completed.")
    elif user_task_selection == -1:
        pass
    else:
        print("You have made an incorrect selection, please try again")
        pass

def gen_reports():
    tasks = []
    users = {}
    completed_tasks = 0
    overdue_tasks = 0

    with open('tasks.txt', 'r') as file:
        for line in file:
            task_data = line.strip().split(';')
            due_date = datetime.strptime(task_data[3], DATETIME_STRING_FORMAT)
            completed = task_data[5] == "yes"
            tasks.append({'assigned_to': task_data[0], 'due_date': due_date, 'completed': completed})

            # Counting the complete and overdue tasks
            if completed:
                completed_tasks += 1
            if not completed and due_date < datetime.now():
                overdue_tasks += 1

            if task_data[0] in users:
                users[task_data[0]]['total_tasks'] += 1
                if completed:
                    users[task_data[0]]['completed_tasks'] += 1
            else:
                users[task_data[0]] = {'total_tasks': 1, 'completed_tasks': 1 if completed else 0}

    total_tasks = len(tasks)
    uncompleted_tasks = total_tasks - completed_tasks

    # Writing to task_overview.txt
    with open('task_overview.txt', 'w') as file:
        file.write(f"Total number of tasks: {total_tasks}\n")
        file.write(f"Total number of completed tasks: {completed_tasks}\n")
        file.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Total number of tasks that have not been completed and are overdue: {overdue_tasks}\n")
        file.write(f"Percentage of tasks that are incomplete: {uncompleted_tasks / total_tasks * 100}%\n")
        file.write(f"Percentage of tasks that are overdue: {overdue_tasks / total_tasks * 100}%\n")

    with open('user.txt', 'r') as file:
        total_users = sum(1 for line in file)

    # Writing to user_overview.txt
    with open('user_overview.txt', 'w') as file:
        file.write(f"Total number of users registered: {total_users}\n")
        file.write(f"Total number of tasks that have been generated and tracked: {total_tasks}\n")
        
        for user, data in users.items():
            user_total_tasks = data['total_tasks']
            user_completed_tasks = data['completed_tasks']
            user_percentage_of_total = (user_total_tasks / total_tasks) * 100 if total_tasks > 0 else 0
            user_percentage_completed = (user_completed_tasks / user_total_tasks) * 100 if user_total_tasks > 0 else 0
            
            file.write(f"\nUser: {user}\n")
            file.write(f"Total number of tasks assigned: {user_total_tasks}\n")
            file.write(f"Percentage of tasks assigned to user: {user_percentage_of_total}%\n")
            file.write(f"Percentage of tasks completed by user: {user_percentage_completed}%\n")

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
       
    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr':
        gen_reports()
                
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        print(line)
        print("\nTask Overview:\n")
        with open('task_overview.txt', 'r') as file:
            for line in file:
                print(line.strip())
        print(line)
        print("\nUser Overview:\n")
        with open('user_overview.txt', 'r') as file:
            for line in file:
                print(line.strip())
        print(line)    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")