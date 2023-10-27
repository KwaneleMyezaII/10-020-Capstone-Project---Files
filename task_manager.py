#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
user_info = []
login = False

while True:
    with open("user.txt", "r+") as file:
        for line in file:
            user_info.append(line.split(", "))

    username = input("Enter username: ")
    password = input("Enter password: ")

    for item in user_info:
        print(item)
        if username == item[0].strip() and password == item[1].strip():
            login = True
            break

    if login == True:
        break

    else:
        print("Enter valid username and password.")


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
st - view number of registered users and the number of tasks
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        if username == "admin":
            with open("user.txt", "a") as file:
                new_username = input("New username: ")
                new_password = input("New password: ")
                confirm_password = input("Confirm password: ")

                if new_password == confirm_password:
                    file.write("\n" + new_username + ", " + new_password)
                else:
                    print("Passwords do not match. Please try again.")

        else:
            print("Only the admin has rights to perform this action!")

    elif menu == 'a':
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        with open("tasks.txt", "a") as file:
            task_username = input("username: ")
            title = input("title: ")
            description = input("description: ")
            due_date = input("due date: ")
            assigned_date = datetime.date.today()
            month_name = assigned_date.strftime('%B')[:3]
            print(month_name)
            new_task = f"\n{task_username}, {title}, {description}, {due_date}, {assigned_date.day} {month_name} {assigned_date.year}, No"
            print(new_task)
            file.write(new_task)

    elif menu == 'va':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        with open("tasks.txt", "r+") as file:
            for line in file:
                task = []
                task = line.split(", ")
                print(f"""Task:             {task[1]}
Assigned to:      {task[0]}
Date assigned:    {task[3]}
Due date:         {task[4]}
Task Complete?    {task[5].strip()}
Task desccription:
 {task[2]}
""")

    elif menu == 'vm':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        
        with open("tasks.txt", "r+") as file:
            for line in file:
                task = []
                task = line.split(", ")

                if task[0] == username:
                    print(f"""Task:             {task[1]}
Assigned to:      {task[0]}
Date assigned:    {task[3]}
Due date:         {task[4]}
Task Complete?    {task[5].strip()}
Task desccription:
 {task[2]}
""")
                    
    elif menu == 'st':
        with open("user.txt", "r+") as file:
            users = 0
            for line in file:
                users += 1

        with open("tasks.txt", "r+") as file:
            tasks = 0
            for line in file:
                tasks += 1

        print(f"""Number of users registered:      {users}
Numbers of tasks:                {tasks}
""")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")
