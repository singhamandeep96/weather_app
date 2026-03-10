def show_menu():
    print("\n=====TO-DO LIST=========")
    print("1. View Tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")


def read_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks= [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks=[]
    return tasks


def write_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


while True:
    show_menu()
    choice= input("Enter your choice: ")

    tasks=read_tasks

    if choice=="1":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\n Your tasks: ")
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")

    elif choice=="2":
        new_task= input("Enter new task:")
        tasks.append(new_task)
        write_tasks(tasks)
        print("task added")

    elif choice=="3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        num= int(input("Enter task number to remove:"))
        if 1<=num<=len(tasks):
            removed=tasks.pop(num -1)
            write_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")
    
    elif choice=="4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again")
