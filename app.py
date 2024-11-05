tasks = []

def addTask():
    task = input("Enter Task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def listTask():
    if not tasks:
        print("No Tasks available")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Choose the # of the task you want to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found. try again.")
    except:
        print("Invalide input. Try again!")

if __name__ == "__main__":
    print("Welcome to ToDo")
    while True:
        print("\n")
        print("Please select an option: ")
        print("--------------------------")
        print("1. add Take")
        print("2. Delete Task")
        print("3. List Taks")
        print("4. Exist")

        choice = input("Enter your choice: ")

        if(choice =="1"):
            addTask()
        elif(choice =="2"):
            deleteTask()
        elif(choice =="3"):
            listTask()
        elif(choice =="4"):
            break
        else:
            print("Invalid input. Please try again.")

        print("Good Bye :D")