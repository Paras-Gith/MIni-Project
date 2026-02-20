

def task():
    tasks = []#empty list
    print("----WELCOME TO THE TO DO LIST----")

    total_task = int(input("enter how many task you wnat to add = "))
    for i in range(1,  total_task+1):# means add task if task is 1 then after loop is 2
        task_name = input(f"enter task{i} = ") #you enter task
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("enter\n1-add\n2-update\n3-delete\n4-view\n5-exit/stop\n"))
        if operation == 1:# add task
            add = input("enter task you want to add = ")
            tasks.append(add)
            print(f"task {add} has been successfully added...")

        elif operation == 2:# update task
            updated = input("enter the task name you want to update = ")
            if updated in tasks:
                up = input("enter new task = ")
                ind = tasks.index(updated)
                tasks[ind] = up
                print(f"updated task{up}")
            else:
                print("task not found")

        elif operation == 3:#delete
            delete = input("enter the task which you want to delete = ")
            if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind]
                print(f"Task {delete} has been deleted....")
            else:
                print("task is not found")

        elif operation == 4:#view
            print(f"Total tasks = {tasks}")

        elif operation == 5:#close
            print("closing the program....")
            break

        else:# zada masti nahi 
            print("invalid error and zada masti aa rahi h ")    

task()


