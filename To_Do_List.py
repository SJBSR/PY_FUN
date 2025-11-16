# Creating a to-do list application

# Defining the to do list function
def to_do_list():
    tasks = []

    while True:
        print ("\nTo-Do List Menu:")
        print ("1. View Tasks")
        print ("2. Add Task")
        print ("3. Remove Task")
        print ("4. Exit")
        choice = input("Choose an option betweem 1-4: ")
        if choice == "1":
            print("\nYour Tasks:")
            for task in tasks:
                print("- " + task)
        elif choice == "2":
            task = input("Enter the task you'd like to add: ")
            tasks.append(task)
        elif choice == "3":
            task = input("Enter the task you'd like to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"'{task}' has been removed from your to-do list.")
            else:
                print(f"'{task}' not found in your to-do list.")
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
