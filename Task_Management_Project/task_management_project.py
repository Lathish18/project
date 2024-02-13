def load_data():
    users = {}
    tasks = {}

    try:
        with open("users.txt", "r") as user_file:
            for line in user_file:
                data = line.strip().split(',')
                if len(data) == 2:
                    username, password = data
                    users[username] = password
    except FileNotFoundError as er:
        print(er)

    try:
        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                username, description, status, priority, deadline, remarks = line.strip().split(',')
                if username not in tasks:
                    tasks[username] = []
                tasks[username].append({
                    "description": description,
                    "status": status,
                    "priority": priority,
                    "deadline": deadline,
                    "remarks": remarks
                })
    except FileNotFoundError as er:
        print(er)

    return users, tasks

def save_data(users, tasks):
    with open("users.txt", "w") as user_file:
        for username, password in users.items():
            user_file.write(f"{username},{password}\n")

    with open("tasks.txt", "w") as task_file:
        for username, user_tasks in tasks.items():
            for task in user_tasks:
                task_file.write(f"{username},{task['description']},{task['status']},"
                                f"{task['priority']},{task['deadline']},{task['remarks']}\n")

def add_task(username):
    description = input('Enter the task: ')
    status = 'ongoing'
    priority = input('Priority: ')
    deadline = input('Deadline: ')
    remarks = input('Remarks: ')

    users, tasks = load_data()

    if username not in tasks:
        tasks[username] = []

    tasks[username].append({
        "description": description,
        "status": status,
        "priority": priority,
        "deadline": deadline,
        "remarks": remarks
    })

    save_data(users, tasks)
    print("Task added successfully.")


def update_task(username):
    tasks = load_data()[1]

    print("Your tasks:")
    for i, task in enumerate(tasks[username]):
        print(f"{i + 1}. {task['description']} - Status: {task['status']}")

    task_index = int(input("Enter the task number to update status: ")) - 1

    if 0 <= task_index < len(tasks[username]):
        new_status = input("Enter the new status (completed/dropped/ongoing): ")
        tasks[username][task_index]["status"] = new_status
        save_data({}, tasks)
        print("Task status updated successfully.")
    else:
        print("Invalid task number.")

def view_task(username):
    users,tasks = load_data()

    if username in tasks:
        user_task = tasks[username]
        if user_task:
            print(f'Tasks for {username}')
            for i, task in enumerate(user_task):
                print(f"{i+1}. {task['description']} - Status: {task['status']}")
    else:
        print(f'No tasks found for {username}')

    print('*******************************')

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users, tasks = load_data()

    if username in users:
        print("Username already exists. Please choose another.")
    else:
        users[username] = password
        tasks[username] = []
        save_data(users, tasks)
        print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users, tasks = load_data()

    if username in users and users[username] == password:
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None

def taskApp():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. View tasks")
        print("4. Add Task")
        print("5. Update Task Status")
        print("6. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                print(f"Hiii, {username}!")
        elif choice == "3" and "username" in locals():
            view_task(username)
        elif choice == "4" and "username" in locals():
            add_task(username)
        elif choice == "5" and "username" in locals():
            update_task(username)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please, Login first!")

taskApp()
