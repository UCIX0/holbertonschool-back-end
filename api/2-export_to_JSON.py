#!/usr/bin/python3
"""Script to use a REST API for a given employee ID, returns
information about his/her TODO list progress and export in JSON"""
import json
import requests
import sys


def export_employee_tasks_to_json(employee_id):
    """Export the tasks of an employee to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee's username and their TODOs
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")

    # Check for valid user
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()
    username = user_data["username"]

    # Construct the tasks list
    tasks_list = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        for task in todos_data
    ]

    tasks_dict = {employee_id: tasks_list}

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(tasks_dict, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <EMPLOYEE_ID>".format(sys.argv[0]))
        sys.exit(1)
    employee_id = sys.argv[1]  # Keep as string for output format
    export_employee_tasks_to_json(employee_id)
