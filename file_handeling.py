# creating a file handeling based project 
# this project will imput data from user and store it in a txt format
# this is will create a data sheet that can read and write a new data 

# <<<<<<<<<<To-do-list>>>>>>>>>>>

import datetime

# function to get date 
def get_date(): 
    return datetime.date.today()

today = get_date

print(today)

def user_data():
    name = input("Enter your name: ")
    task_name = input("enter task name: ")
    n = int(input("enter number of tasks for the day: "))
    for i in range(n):
        task = input("Enter the task of the day: ")

    print("Wecome", name)
    print(f"Your tasks for {task_name} are: ")
    for i in range(n):
        print("#" , task)

# Giving choice for save or edit the file

# def response_choice():
    
    choice = input("ENTER 's' FOR SAVE & 'e' FOR EDIT >>>")

    while True:

        if (choice=='s' or choice=='S'):
            with open(task_name + ".txt", "a" ) as f:
                f.write(f"Wecome {name}\n")
                f.write(f"Your tasks for {task_name} are: \n")
                f.write(f"# {task}\n")

            print("SUCCESSFULLY SAVED!! \n")
            break

        elif (choice=='e' or choice=="E"):
            name = input("Edit your name: ")
            task_name = input("Edit your task name: ")
            n = input("Edit task number: ")
        for i in range(n):
            task = input("Edit task: ")

            with open(task_name + ".txt", "a" ) as f:
                f.write(f"Wecome {name}\n")
                f.write(f"Your tasks for {task_name} are: \n")
                f.write(f"# {task}\n")

            print("SUCCESSFULLY SAVED!! \n")
            break

        else:
            print("INVALID INPUT !!!")
            break

# print the data

def print_data():
    task_name = input("Enter the task name: ")

    try:
        with open(task_name + ".txt" , "r") as f:
            data = f.readlines()
            data = ''.join(data)
            print(data)
    
    except:
        print("DATA NOT FOUND !!")

print("<<<<<<<<< Welcome to To-do-list >>>>>>>>")

while True:
    print("Please choose an option correctly.\n")
    opt= int(input("Enter 1 for add your data, enter 2 for see your data : "))

    if opt== 1:
        user_data()
        break

    elif opt== 2:
        print_data()
        break
    else:
        print("INVALID OPTION CHOOSEN !!!")
