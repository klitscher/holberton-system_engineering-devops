#!/usr/bin/python3
"""Module to connect to an api and grab data"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    # Grab data from website
    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    )
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    )
    # Convert data to JSON
    employee_dict = employee.json()
    todo_list = todo.json()
    # Save data
    json_data = {}
    task_data = []
    task_new_dict = {}
    for task in todo_list:
        task_new_dict = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': employee_dict.get('username'),
        }
        task_data.append(task_new_dict)
    json_data = {sys.argv[1]: task_data}
    # Export data to json
    with open('{}.json'.format(sys.argv[1]), 'w') as employee:
        json.dump(json_data, employee)
