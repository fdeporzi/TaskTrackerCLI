def main():
    print("Welcome to Task CLI")
    print("Type 'help' to see the list of commands")

    while True:
        user_input = input("Enter a command: ")

        #exit command
        if user_input.lower() == "exit":
            print("Exiting Task CLI...")
            break

if __name__ == "__main__":
    main()








# 1. create loop to keep the program running
# 2. get user input
# 3. check if user input is valid
# 4. if valid, run the command
# 5. if invalid, print error message



# add, update delete tasks
# list tasks
# mark tasks as done or in progress
# list tasks that are done
# list tasks that are in progress
# list tasks that are not done

"""
You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.
"""