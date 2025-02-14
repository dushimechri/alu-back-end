#!/usr/bin/python3
"""
Request from API; Return TODO list progress given employee ID
Export this data to CSV
"""
import csv
import requests
from sys import argv


def get_employee_tasks(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch data for employee {employee_id}")
        return
    
    tasks = response.json()
    
    # Get employee name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        employee_name = user_response.json()['name']
    else:
        print(f"Failed to fetch employee data for {employee_id}")
        return

    # Export data to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_tasks(employee_id)
