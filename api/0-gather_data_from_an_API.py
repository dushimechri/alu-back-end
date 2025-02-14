#!/usr/bin/python3

"""
This is the first file I created for the APIs
"""
import sys
import requests 

""" Functions for gathering  data from an API """

employee_id = sys.argv[1]
employe_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
employe_response = requests.get(employe_url)
if employe_response.status_code != 200:
    print("there is no information of this employee")
    sys.exit(1)
else:
    employee_data = employe_response.json()
todo_response = requests.get(todos_url)
if todo_response.status_code != 200:
    print("there is no task of this employee")
    sys.exit(1)
else:
    task_data = todo_response.json()
employe_name = employee_data['name']
number_of_done_tasks = 0
number_of_undone_tasks = 0
for task in task_data:
    if task['completed'] == True:
        number_of_done_tasks += 1
    else:
        number_of_undone_tasks += 1
total_number_of_tasks = number_of_done_tasks + number_of_undone_tasks
print(f"Employee {employee_data['name']} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
titles = []
for task in task_data:
     if task['completed'] == True:
          titles.append(task['title'])
for i in titles:
    print(f"\t {i}")
