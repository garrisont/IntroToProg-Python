# def write_data_to_file(file_name, list_of_rows):
file_name =  "ToDoFile.txt"
list_of_rows = [{'Task': 'mow lawwwwwn', 'Priority': 'high'},\
                {'Task': 'go to work', 'Priority': 'high'},\
                {'Task': 'make dinner', 'Priority': 'med'}, \
                {'Task': 'sleep', 'Priority': 'high'}]
""" Writes data from a list of dictionary rows to a File

:param file_name: (string) with name of file:
:param list_of_rows: (list) you want filled with file data:
:return: (list) of dictionary rows
"""
# TODO: Add Code Here!
objFile = open(file_name, "w")
for dicRow in list_of_rows:
    objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
objFile.close()

# return list_of_rows
