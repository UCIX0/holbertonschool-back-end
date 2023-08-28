#!/usr/bin/env python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Get the TODO progress for a specific employee."""
    # Base URL for the JSON placeholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make API calls to fetch employee's name, and their TODOs
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")

    # Check if user exists
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    # Extract data from API responses
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data["name"]

    # Filter done tasks and calculate numbers
    done_tasks = [task for task in todos_data if task["completed"]]
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todos_data)

    # Print results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in done_tasks:
        print("\t", task["title"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <EMPLOYEE_ID>".format(sys.argv[0]))
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
