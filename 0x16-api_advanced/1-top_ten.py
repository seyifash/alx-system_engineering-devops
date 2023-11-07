#!/usr/bin/python3
"""gets the top ten posts"""
import requests


def top_ten(subreddit):
    """ gets the top ten post title"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        'User-Agent': 'YourBotName/1.0 (by YourUsername)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
