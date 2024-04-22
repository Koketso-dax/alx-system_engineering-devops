#!/usr/bin/python3
"""
module to write TODO's
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Get employee's stored items
    """
    strUserResponse = "https://jsonplaceholder.typicode.com/users/{}"
    user_response = requests.get(strUserResponse.format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get('name')

    strTodoResponse = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todos_response = requests.get(strTodoResponse.format(employee_id))
    todos_data = todos_response.json()

    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos_data)

    print("Employee {} is done with tasks ({}/{total}):"
          .format(employee_name, num_completed_tasks, total=total_num_tasks))
    for task in completed_tasks:
        print("\t{}".format(task['title']))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
