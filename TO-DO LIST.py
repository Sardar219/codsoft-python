# To-Do List Program in Python

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_item(new_task, task_list):
    task_list.append(new_task)
    with open('tasks.txt', 'a') as file:
        file.write(new_task + '\n')

# Function to delete a task
def delete_item(task_list):
    selected_task_index = tasks.index(task_list.get(task_list.curselection()))
    del tasks[selected_task_index]
    task_list.delete(task_list.curselection())
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Main function
if __name__ == "__main__":
    # Read existing tasks from the file
    with open('tasks.txt', 'r') as file:
        tasks = [line.strip() for line in file]

    # Display tasks
    print("Welcome to your To-Do List!")
    for task in tasks:
        print(f"- {task}")

    # User interaction loop
    while True:
        user_input = input("\nWhat would you like to do? (add/delete/quit): ").lower()
        if user_input == "add":
            new_task = input("Enter the task you want to add: ")
            add_item(new_task, tasks)
        elif user_input == "delete":
            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            task_index = int(input("Enter the task number you want to delete: ")) - 1
            delete_item(task_index, tasks)
        elif user_input == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'add', 'delete', or 'quit'.")
