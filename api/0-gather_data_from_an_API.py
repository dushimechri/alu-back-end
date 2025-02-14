#!/usr/bin/python3

"""
This script gathers and processes data from the JSONPlaceholder API for a given employee ID.
It fetches the employee's details and their TODO list, calculates the number of completed and 
incomplete tasks, and then displays the results.

Modules:
        sys (standard library) - used to read the employee ID from command-line arguments.
        requests (third-party library) - used to make HTTP requests to fetch employee data and tasks.
"""

import sys
import requests 


def fetch_data():
    """main function"""
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

if __name__ == '__main__':
        fetch_data()
