#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
"""
import csv
import re
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            e_id = int(sys.argv[1])
            REST_API = "https://jsonplaceholder.typicode.com"
            emp_req = requests.get('{}/users/{}'.format(REST_API, e_id)).json()
            do_req = requests.get('{}/todos'.format(REST_API)).json()
            filename = "{}.csv".format(e_id)
            with open(filename, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for task in do_req:
                    if task.get("userId") == e_id:
                        csv_writer.writerow([task["userId"],
                                            emp_req["username"],
                                            task["completed"],
                                            task["title"]])
