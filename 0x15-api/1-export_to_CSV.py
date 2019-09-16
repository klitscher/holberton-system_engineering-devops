#!/usr/bin/python3
"""Module to connect to an api and grab data"""

import csv
import requests
import sys

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
employee_name = employee_dict.get('name')
number_of_tasks = len(todo_list)
completed_tasks = [dic for dic in todo_list if dic.get('completed') is True]
# Export data to csv
with open('{}.csv'.format(sys.argv[1]), 'w') as task:
    task_writer = csv.writer(
        task,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    for dic in todo_list:
        task_writer.writerow([
            employee_dict.get('id'),
            employee_dict.get('username'),
            dic.get('completed'),
            dic.get('title')
        ])
