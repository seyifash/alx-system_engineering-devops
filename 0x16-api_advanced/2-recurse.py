#!/usr/bin/python3
"""gets all hot post"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """gets all hot post by using pagiination"""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
            subreddit, after)
    headers = {
        'User-Agent': 'YourBotName/1.0 (by YourUsername)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
