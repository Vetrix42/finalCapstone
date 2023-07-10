import datetime

# File names
USER_FILE = "users.txt"
TASK_FILE = "tasks.txt"
TASK_OVERVIEW_FILE = "task_overview.txt"
USER_OVERVIEW_FILE = "user_overview.txt"

# Helper function to read data from a file
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read().splitlines()
        return data
    except FileNotFoundError:
        return []

# Helper function to write data to a file
def write_file(file_name, data, mode="w"):
    with open(file_name, mode) as file:
        for item in data:
            file.write(f"{item}\n")

# Helper function to check if a date is valid
def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Helper function to get the current date
def current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# Function to register a new user
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm password: ")

    # Check if the password and confirm password match
    if password == confirm_password:
        users = read_file(USER_FILE)
        usernames = [user.split(":")[0] for user in users]
        if username in usernames:
            print("Username already exists. Please try again.")
        else:
            user = f"{username}:{password}"
            users.append(user)
            write_file(USER_FILE, users, mode="a")
            print("User registered successfully.")
            return True
    else:
        print("Passwords do not match. Please try again.")

    return False

# Function to login a user
def login_user():
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        users = read_file(USER_FILE)
        for user in users:
            user_details = user.split(":")
            if user_details[0] == username and user_details[1] == password:
                print("Login successful.")
                return username  # Return the logged-in username

        print("Invalid username or password. Please try again.")
        attempts += 1

    print("Maximum login attempts exceeded.")
    return None

# Function to add a new task
def add_task():
    tasks = read_file(TASK_FILE)

    username = input("Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter a description of the task: ")
    task_due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

    # Check if the due date is valid
    if not is_valid_date(task_due_date):
        print("Invalid due date format. Please enter a valid date in the format YYYY-MM-DD.")
        return

    task = f"{task_title};{task_description};{task_due_date};No;{username}"
    tasks.append(task)
    write_file(TASK_FILE, tasks, mode="a")
    print("Task added successfully.")

# Function to view all tasks
def view_all():
    tasks = read_file(TASK_FILE)

    if tasks:
        print("All Tasks\n")
        for index, task in enumerate(tasks, start=1):
            task_details = task.split(";")
            print(f"Task {index}:")
            print(f"Title: {task_details[0]}")
            print(f"Assigned to: {task_details[4]}")
            print(f"Description: {task_details[1]}")
            print(f"Due Date: {task_details[2]}")
            print(f"Completed: {task_details[3]}")
            print()
    else:
        print("No tasks available.")

# Function to view tasks assigned to the user
def view_mine(username):
    tasks = read_file(TASK_FILE)
    user_tasks = []

    for task in tasks:
        task_details = task.split(";")
        if task_details[4] == username:
            user_tasks.append(task)

    if user_tasks:
        print(f"Tasks assigned to {username}\n")
        for index, task in enumerate(user_tasks, start=1):
            task_details = task.split(";")
            print(f"Task {index}:")
            print(f"Title: {task_details[0]}")
            print(f"Description: {task_details[1]}")
            print(f"Due Date: {task_details[2]}")
            print(f"Completed: {task_details[3]}")
            print()
    else:
        print(f"No tasks assigned to {username}.")

# Function to generate the task overview report
def generate_task_overview():
    tasks = read_file(TASK_FILE)
    task_overview = []

    for task in tasks:
        task_details = task.split(";")
        task_overview.append(f"{task_details[0]};{task_details[4]};{task_details[2]};{task_details[3]}")

    write_file(TASK_OVERVIEW_FILE, task_overview)

# Function to generate the user overview report
def generate_user_overview():
    users = read_file(USER_FILE)
    tasks = read_file(TASK_FILE)
    user_overview = []

    for user in users:
        user_details = user.split(":")
        user_tasks = [task for task in tasks if task.split(";")[4] == user_details[0]]
        user_overview.append(f"{user_details[0]};{len(user_tasks)};{len([task for task in user_tasks if task.split(';')[3] == 'Yes'])}")

    write_file(USER_OVERVIEW_FILE, user_overview)

# Main program
def main():
    logged_in_user = None

    # Login or register a user
    while logged_in_user is None:
        choice = input("Enter 'login' to log in or 'register' to register a new user: ")

        if choice.lower() == "login":
            logged_in_user = login_user()
        elif choice.lower() == "register":
            registered = register_user()
            if registered:
                logged_in_user = login_user()
        else:
            print("Invalid choice. Please try again.")

    # Check if the logged-in user is the admin
    if logged_in_user == "admin":
        while True:
            admin_choice = input(
                "Enter 'r' to register a new user, 'a' to add a new task, 'va' to view all tasks,"
                "'vm' to view my tasks, 'gr' to generate reports, or 'logout' to log out: "
            )

            if admin_choice.lower() == "r":
                register_user()
            elif admin_choice.lower() == "a":
                add_task()
            elif admin_choice.lower() == "va":
                view_all()
            elif admin_choice.lower() == "vm":
                view_mine(logged_in_user)
            elif admin_choice.lower() == "gr":
                generate_task_overview()
                generate_user_overview()
                print("Reports generated successfully.")
            elif admin_choice.lower() == "logout":
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        while True:
            user_choice = input(
                "Enter 'a' to add a new task, 'va' to view all tasks,"
                "'vm' to view my tasks, or 'logout' to log out: "
            )

            if user_choice.lower() == "a":
                add_task()
            elif user_choice.lower() == "va":
                view_all()
            elif user_choice.lower() == "vm":
                view_mine(logged_in_user)
            elif user_choice.lower() == "logout":
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
