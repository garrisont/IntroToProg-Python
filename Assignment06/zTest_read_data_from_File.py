# def read_data_from_file(file_name, list_of_rows):

file_name =  "ToDoFile.txt"
list_of_rows = []

list_of_rows.clear()  # clear current data

# Check if file exists
import os
isPath = os.path.exists(file_name)
if not isPath:
    file = open(file_name, "a")  # file missing, create a blank one
    file.close()

file = open(file_name, "r")
for line in file:
    task, priority = line.split(",")
    row = {"Task": task.strip(), "Priority": priority.strip()}
    list_of_rows.append(row)
file.close()

print(list_of_rows)