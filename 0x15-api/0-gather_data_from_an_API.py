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
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    completed_tasks = [todo for todo in todos_data if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
