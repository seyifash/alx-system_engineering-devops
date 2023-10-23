#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
"""
import json
import re
import requests
import sys


if __name__ == "__main__":
    REST_API = "https://jsonplaceholder.typicode.com"
    emp_req = requests.get('{}/users'.format(REST_API)).json()
    filename = "todo_all_employees.json"
    all_emp_task = {}
    for emps in emp_req:
        e_id = emps["id"]
        do_req = requests.get('{}/todos?userId={}'.format
                              (REST_API, e_id)).json()
        json_data = [
            {
                "username": emps["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in do_req
            ]

        all_emp_task[e_id] = json_data
    with open(filename, 'w') as json_file:
        json.dump(all_emp_task, json_file)
