def main():
    options = {
        1:"Add task",
        2:"Remove task",
        3:"Show tasks",
        4:"Quit"
    }
    tasks = ["sigma", "ligma"]
    print("To Do List App:")
    for num, opt in options.items():
        print(f"{num}. {opt}")
        
    while True:
        try:
            option = input("> ")
            option = int(option)
            
            if option not in options.keys():
                raise ValueError("Invalid option")
            
            match option:
                case 1: # Add task
                    new_task = input("New task: ")
                    tasks.append(new_task)
                    print(tasks)
                case 2: # Remove task
                    if not tasks:
                        print("No taks to remove")
                        break
                    for i, t in enumerate(tasks, 1):
                        print(f"{i}. {t}")
                    try:
                        task_to_remove = int(input("Remove task: "))
                        if task_to_remove < 1 or task_to_remove > len(tasks):
                            raise ValueError("Invalid option")
                        removed = tasks.pop(task_to_remove - 1)
                        print(f"Removed task \"{removed}\"")
                    except ValueError as e:
                        print("Error:", e)
                case 3: # Show task
                    if not tasks:
                        print("No tasks to show")
                        
                    for i, t in enumerate(tasks, 1):
                        print(f"{i}. {t}")
                case 4: # Quit
                    print("Quitting...")
                    break
        except ValueError as e:
            print("Error:", e)
    
if _name_ == '__main__':
    main() 