import json
import os
import sys
from datetime import datetime

# TODO: List task function


def main():
    print("Welcome to Task CLI")
    print("Type 'help' to see the list of commands")

    while True:
        user_input = input("\nEnter a command: ")

        #exit command
        if user_input.lower() == "exit":
            print("Exiting Task CLI...")
            break

        #splits input with command and argument
        parts = user_input.split()
        #checks if parts is empty
        if not parts:
            print("Please enter a command")
            continue

        command = parts[0] #command is the first part of the input
        args = parts[1:] #argument

        if command == "help":
            print("Available commands:")
            print("add <task>")
            print("update <task_id> <new_task>")
            print("delete <task_id>")
            print("list")
            print("mark-done <task_id>")
            print("mark-in-progress <task_id>")
            print("list done")
            print("list not-done")
            print("list in-progress")
            print("exit")

        
        elif command == "add":
            if len(args) < 1: #shows error if no task is entered
                print("Please use format: add \"task descritpion\"")
            else:
                description = " ".join(args) #joins the arguments to form a single string
                print(f"Adding task: {description}")

                add_task(description) #calls add_task function

        
        elif command == "list":
            status_filter = args[0] if args else None #checks if there is an argument for a task status and assigns it to status_filter
            print(f"Listing tasks" + (f" with status: {status_filter}" if status_filter else ""))
            # call list_tasks function here
            list_tasks(status_filter)

        #add more command handlers here
        elif command == "update":
            if len(args) < 2:
                print("Please use format: update <task_id> <new_task>")
            else:
                task_id = int(args[0])
                new_description = " ".join(args[1:])
                print(f"Updating task {task_id} to: {new_description}")

                # call update_task function here

        elif command == "delete":
            if len(args) < 1:
                print("Please use format: delete <task_id>")
            else:
                task_id = int(args[0])
                print(f"Deleting task {task_id}")

                # call delete_task function here

        elif command == "mark-done":
            if len(args) < 1:
                print("Please use format: mark-done <task_id>")
            else:
                task_id = int(args[0])
                print(f"Marking task {task_id} as done")

                # call mark_done_task function here

        elif command == "mark-in-progress":
            if len(args) < 1:
                print("Please use format: mark-in-progress <task_id>")
            else:
                task_id = int(args[0])
                print(f"Marking task {task_id} as in-progress")

                # call mark_in_progress_task function here

        else:
            print(f"Unknown command: {command}")
            print("Available commands: add, list, update, delete, mark-in-progress, mark-done")



def load_tasks():
    # check if tasks.json exists
    if not os.path.exists("tasks.json"):
        return []

    # read tasks from file
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    return tasks

def save_tasks(tasks):
    # write tasks to file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    # load tasks from file
    tasks = load_tasks()

    # create new task
    new_task = {
        "id": generate_task_id(),
        "description": description,
        "status": "not-done",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    # add new task to tasks
    tasks.append(new_task)

    # save tasks to file
    save_tasks(tasks)

    print("Task added successfully")


def generate_task_id():
    tasks = load_tasks()

    # if tasks is empty, give new task id of 1
    if not tasks:
        return 1

    # get the last task id and increment by 1
    return tasks[-1]["id"] + 1

def list_tasks(status_filter=None):
    tasks = load_tasks()

    for task in tasks:
        if status_filter and task["status"] != status_filter:
            continue

        print(f'{task["id"]}: {task["description"]} ({task["status"]})')

if __name__ == "__main__":
    main()


