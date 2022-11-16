# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# TGarrison,2022-11-15,Added code to complete assignment 5
#                      Note - used json file to simplify read/write
# ------------------------------------------------------------------------ #

import json  # 

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
strData = ""  # A row of text data from the file
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """  
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save changes to file
    5) Exit Program
    """   # A menu of user options
# ^ (added it here because I think that's what's being asked of us?)
#   (not sure it's actually cleaner in this case)
strChoice = "" # A Capture the user option selection
lstLines = [] # A list containing starting file lines
strTask = "" # A temporary container for Task
strPriority = "" # A temporary container for Priority


# -- Processing -- #
try:
    # Read in the file lines with one file open/close
    f = open(objFile, "r")
    # fLines = f.read().splitlines() # Commented out after switching to json format
    lstTable = json.load(f)  # **Read data into table of dictionaries
    f.close()

except:
    # File must not exist, create it add header, then open for reading
    print("File \'" + objFile + "\' not found.")
    print("(current data is blank)")

# for row in fLines:  ##  Obsolete with use of json format #
#     strTask, strPriority = row.split(",", )
#     lstTable.append({"Task":strTask.strip(), "Priority":strPriority.strip()})

# -- Input/Output -- #
# Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # 1 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("==============")
        print("Task, Priority")
        print("--------------")
        for entry in lstTable:
            print(entry["Task"] +", " + entry["Priority"])
        print("==============")

    # 2-  Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str(input("New task: "))
        strPriority = str(input("Priority of new task: "))
        lstTable.append({"Task": strTask.strip(), "Priority": strPriority.strip()})

    # 3 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = str(input("Enter task to remove:  "))
        for dicRow in lstTable:
            if dicRow["Task"].strip().lower() == strTask.strip().lower():
                lstTable.remove(dicRow)
                break # Break the for loop only
        else:   # else for the for loop :)
            print("Failed to remove \'" + strTask + "\'")

    # 4 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        f = open(objFile, "w")
        f.write(json.dumps(lstTable))
        f.close()

    # 5 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
