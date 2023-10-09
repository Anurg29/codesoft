# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print("Task added:", task)

# Function to view the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to mark a task as done
def mark_done(task_index):
    if 1 <= task_index <= len(todo_list):
        task = todo_list[task_index - 1]
        print(f"Task '{task}' marked as done.")
        todo_list.pop(task_index - 1)
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nOptions:")
    print("Enter 'add' to add a task")
    print("Enter 'view' to view your to-do list")
    print("Enter 'done' to mark a task as done")
    print("Enter 'quit' to quit the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Enter a task: ")
        add_task(task)
    elif user_input == "view":
        view_tasks()
    elif user_input == "done":
        task_index = int(input("Enter the task number to mark as done: "))
        mark_done(task_index)
    else:
        print("Invalid input. Please try again.")
