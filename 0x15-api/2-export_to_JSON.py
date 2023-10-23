#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
"""
import json
import re
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            e_id = int(sys.argv[1])
            REST_AP = "https://jsonplaceholder.typicode.com"
            emp_req = requests.get('{}/users/{}'.format(REST_AP, e_id)).json()
            do_req = requests.get('{}/todos?userId={}'.format(
                                                         REST_AP, e_id)).json()
            filename = "{}.json".format(e_id)
            json_data = {
                emp_req["id"]: [
                    {
                        "task": task["title"],
                        "completed": task["completed"],
                        "username": emp_req["username"]
                    }
                    for task in do_req
                    ]
                }
            with open(filename, 'w') as json_file:
                json.dump(json_data, json_file)
