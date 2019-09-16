#!/usr/bin/python3
"""Module to connect to an api and grab data"""

import csv
import json
import requests
import sys


if __name__ == '__main__':
    # Grab data from website
    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users'
    )
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
    )
    # Convert data to JSON
    employee_dict = employee.json()
    todo_list = todo.json()
    # Save data
    json_data = {}
    task_data = []
    task_new_dict = {}
    for employee in employee_dict:
        for task in todo_list:
            if employee.get('id') == task.get('userId'):
                task_new_dict = {
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                    'username': employee.get('username'),
                }
                task_data.append(task_new_dict)
        json_data['{}'.format(employee.get('id'))] = task_data
        task_data = []
    # Export data to json
    with open('todo_all_employees.json', 'w') as employees:
        json.dump(json_data, employees)
