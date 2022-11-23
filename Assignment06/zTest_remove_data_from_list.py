# def remove_data_from_list(task, list_of_rows):

task = "mo lawn"
list_of_rows = [{'Task': 'mow lawn', 'Priority': 'high'},\
                {'Task': 'go to work', 'Priority': 'high'},\
                {'Task': 'make dinner', 'Priority': 'med'}, \
                {'Task': 'sleep', 'Priority': 'high'}]

""" Removes data from a list of dictionary rows

:param task: (string) with name of task:
:param list_of_rows: (list) you want filled with file data:
:return: (list) of dictionary rows
"""
# TODO: Add Code Here!
for row in list_of_rows:
    if row["Task"].strip().lower() == task.strip().lower():
        list_of_rows.remove(row)
        print("Removed \'" + task + "\'")
        break  # Break the for loop only
else:  # else for the for loop :)
    print("Failed to remove \'" + task + "\'")

# return list_of_rows
print(list_of_rows)