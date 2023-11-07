#!/usr/bin/python3
"""checks for all subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ Define the Reddit API URL for the given subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        'User-Agent': 'YourBotName/1.0 (by YourUsername)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
