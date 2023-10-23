#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
"""
import sys
import requests
import re

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            e_id = int(sys.argv[1])
            REST_API = "https://jsonplaceholder.typicode.com"
            emp_req = requests.get('{}/users/{}'.format(REST_API, e_id)).json()
            do_req = requests.get('{}/todos'.format(REST_API)).json()
            empl_name = emp_req.get('name')
            the_tasks = [task for task in do_req if task.get('userId') == e_id]
            compl_task = [task for task in the_tasks if task["completed"]]
            print('Employee {} is done with tasks({}/{}):'.format(
                                                            empl_name,
                                                            len(compl_task),
                                                            len(the_tasks)))
            if len(compl_task) > 0:
                for task in compl_task:
                    print('\t {}'.format(task.get('title')))
