#!/usr/bin/python3
"""Module to connect to an api and grab data"""

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
# Print data in format specified
print('Employee {} is done with tasks({}/{}):'.format(
    employee_name,
    len(completed_tasks),
    number_of_tasks)
  )
for task in completed_tasks:
    print('\t{}'.format(task.get('title')))
