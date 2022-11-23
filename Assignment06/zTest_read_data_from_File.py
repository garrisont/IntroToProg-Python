# def read_data_from_file(file_name, list_of_rows):

file_name =  "ToDoFile.txt"
list_of_rows = []

list_of_rows.clear()  # clear current data
file = open(file_name, "r")
for line in file:
    task, priority = line.split(",")
    row = {"Task": task.strip(), "Priority": priority.strip()}
    list_of_rows.append(row)
file.close()

print(list_of_rows)