# def add_data_to_list(task, priority, list_of_rows):
""" Adds data to a list of dictionary rows

:param task: (string) with name of task:
:param priority: (string) with name of priority:
:param list_of_rows: (list) you want filled with file data:
:return: (list) of dictionary rows
"""

task = "sleep"

priority = "high"

list_of_rows = [\
    {'Task': 'mow lawn', 'Priority': 'high'},\
    {'Task': 'go to work', 'Priority': 'high'},\
    {'Task': 'make dinner', 'Priority': 'med'}\
    ]

row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
list_of_rows.append( row )

print(list_of_rows)
# return list_of_rows
