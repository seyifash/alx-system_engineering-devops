#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ Define the Reddit API URL for the given subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid being blocked
    headers = {
        'User-Agent': 'YourBotName/1.0 (by YourUsername)'
    }

    # Send a GET request to the Reddit API without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check the response status code
    if response.status_code == 200:
        try:
            # Parse the JSON response and extract the subscriber count
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            # Handle JSON parsing errors
            return 0
    else:
        # Handle invalid subreddit or other errors
        return 0
