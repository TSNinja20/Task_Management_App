def task():
    tasks = [] #empty list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    total_task = int(input("Enter how many task you want to add = ")) #5
    for i in range(1,total_task+1):
        task_name = input(f"Entr task {i} = ") #enter task 1=
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")
    while True:
        print("\nChoose your task:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/\n")
        operation = int(input("Enter your task:"))
    
        if operation == 1:
            add = input("Enter task you weant to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")


        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val) #2
                tasks[ind] = up
                print(f"updated task {up}")

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")

        elif operation == 4:
            print(f"Total tasks ={tasks}")

        elif operation == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid Input")


task()

